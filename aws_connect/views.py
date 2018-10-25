import csv
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from datetime import datetime

from aws_connect.models import Department, AppointmentReport, Patient
from aws_connect.utils.files import save_file
from aws_connect.consts import PATIENT_DETAILS_HEADERS

def index(request):
    departments = Department.objects.values('dept_key', 'dept_name').distinct()
    apt_min_date = AppointmentReport.objects.earliest('appt_start_datetime').appt_start_datetime.strftime("%m/%d/%y")
    apt_max_date = AppointmentReport.objects.latest('appt_start_datetime').appt_start_datetime.strftime("%m/%d/%y")
    return render(request, 'base.html', {'departments': departments, 'min_date': apt_min_date, 'max_date': apt_max_date})

def get_appts(request):
    appts = dict()
    columns = ['rep_appt_key', 'appt_start_datetime', 'appt_duration', 'patient_key__patient_first_name', 'patient_key__patient_last_name', 'prob_no_show', 'status']
    daterange = [datetime.strptime(date_var, '%m/%d/%Y') for date_var in request.GET['daterange'].split(' - ')]

    if request.GET['dept'] != '':
        appts = AppointmentReport.objects \
                .filter(dept_key=request.GET['dept'], appt_start_datetime__range=daterange) \
                .values('rep_appt_key', 'appt_start_datetime', 'appt_duration', 'patient_key__patient_first_name', 'patient_key__patient_last_name', 'prob_no_show', 'status')
    return appts
    
def get_patient_details(request):
    appts = get_appts(request)

    return render(request, 'table.html', {'rows': appts, 'headers': PATIENT_DETAILS_HEADERS})

def download_csv(request):
    appts = get_appts(request)
    csv_headers = ['Appt. ID'] + PATIENT_DETAILS_HEADERS

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="patient_access.csv"'

    writer = csv.writer(response)
    writer.writerow(csv_headers)

    for appt in appts:
        writer.writerow(appt.values())

    return response

def update_status(request):
    appt_key = request.GET['appt_key']
    status = request.GET['status']

    curr_appt = AppointmentReport.objects.get(rep_appt_key=appt_key)
    curr_appt.update_status(status)

    return True