from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from aws_connect.models import SuperGroup, FileHandler
from aws_connect.consts import SUPER_GROUP_S3_FOLDER
from aws_connect.utils.files import save_file

def index(request, new_recs=None):
    super_groups = SuperGroup.objects.values('super_group').distinct()
    return render(request, 'base.html', {'super_groups': super_groups, 'new_recs': new_recs})

def get_cpt_groups(request, super_group):
    cpt_groups = SuperGroup.objects.filter(super_group=super_group)
    return render(request, 'cpt_groups.html', {'groups': cpt_groups})

def upload_group_file(request):
    if request.method == 'POST':
        created_count = 0
        file_info = request.FILES['file']
        file_name = file_info.name
        file_bytes = file_info.read()
        file_data = file_bytes.decode('utf-8')

        for data_row in file_data.split('\r')[1:]:
            fields = data_row.split(',')
            obj, created = SuperGroup.objects.get_or_create(super_group=fields[1], primary_cpt_group=fields[2])
            if created == True:
                created_count += 1
    
        if created_count > 0:
            file_rec = save_file(settings.AWS_S3_BUCKET, SUPER_GROUP_S3_FOLDER, file_name, file_bytes)
    else:
        return redirect('main')

    return redirect('notify', new_recs=created_count)