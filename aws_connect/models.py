from django.db import models
from django.conf import settings
from datetime import datetime


class Department(models.Model):
    dept_key = models.IntegerField(primary_key=True, null=False, db_column='dept_key')
    dept_name = models.TextField()
    practice_key = models.IntegerField()
    not_in_data = models.IntegerField()
    note = models.TextField()
    
    class Meta:
        db_table = 'dim\".\"dept'
        managed = False

class Patient(models.Model):
    patient_key = models.IntegerField(primary_key=True, null=False, db_column='patient_key')
    patient_prefix = models.TextField()
    patient_first_name = models.TextField()
    patient_middle_name = models.TextField()
    patient_last_name = models.TextField()
    patient_suffix = models.TextField()
    patient_date_of_birth = models.DateField()
    patient_ssn = models.TextField()
    patient_phone = models.TextField()
    patient_address1 = models.TextField()
    patient_address2 = models.TextField()
    patient_city = models.TextField()
    patient_state = models.TextField()
    patient_zip = models.TextField()
    patient_longitude = models.FloatField()
    patient_latitude = models.FloatField()
    patient_gender_grpa1_key = models.IntegerField()
    patient_race_grpa1_key = models.IntegerField()

    @property
    def patient_name(self):
        return '{} {}'.format(self.patient_first_name, self.patient_last_name)

    class Meta:
        db_table = 'dim\".\"patient'
        managed = False


class Practice(models.Model):
    practice_key = models.IntegerField(primary_key=True, null=False)
    practice_name = models.TextField()
    practice_description = models.TextField()
    note = models.TextField()

    class Meta:
        db_table = 'dim\".\"practice'
        managed = False


class Personnel(models.Model):
    personnel_key = models.IntegerField(primary_key=True, null=False)
    prefix = models.TextField()
    first_name = models.TextField()
    middle_name = models.TextField()
    last_name = models.TextField()
    suffix = models.TextField()
    npi = models.TextField()
    job_code_key = models.IntegerField()
    comp_type_key = models.IntegerField()
    home_dept_key = models.IntegerField()
    gender_key = models.IntegerField()
    birth_date = models.DateTimeField()
    start_date = models.DateTimeField()
    term_date = models.DateTimeField()
    term_reason_key = models.IntegerField()

    primary_location_key = models.IntegerField()
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zip_code = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    note = models.TextField()

    class Meta:
        db_table = db_table = 'dim\".\"personnel'
        managed = False


class VisitType(models.Model):
    visit_type_key = models.IntegerField(primary_key=True, null=False)
    system_key = models.IntegerField()
    visit_type_id = models.TextField()
    visit_type_desc = models.TextField()
    note = models.TextField()

    class Meta:
        managed = False
        db_table = db_table = 'dim\".\"visit_type'


class AppointmentReport(models.Model):
    rep_appt_key = models.IntegerField(primary_key=True, null=False)
    patient_key = models.ForeignKey(Patient, db_column='patient_key', on_delete=models.DO_NOTHING)
    personnel_key = models.ForeignKey(Personnel, db_column='personnel_key', on_delete=models.DO_NOTHING)
    dept_key = models.ForeignKey(Department, db_column='dept_key', on_delete=models.DO_NOTHING)
    visit_type_key = models.ForeignKey(VisitType, db_column='visit_type_key', on_delete=models.DO_NOTHING)
    appt_start_datetime = models.DateTimeField()
    appt_duration = models.IntegerField()
    noshow_grouping = models.TextField()
    appt_lag_grouping = models.TextField()
    hhi_grouping = models.TextField()
    distance_grouping = models.TextField()
    payer_grouping = models.TextField()
    inpatient_indicator = models.IntegerField()
    prob_no_show = models.FloatField()
    note = models.TextField()
    create_date = models.DateTimeField(default=datetime.now())
    create_user = models.TextField()

    class Meta:
        db_table = 'rep\".\"appt'
        managed = False