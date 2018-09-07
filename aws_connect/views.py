from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from aws_connect.utils import s3
from aws_connect.models import SuperGroup

def index(request, new_recs=None):
    super_groups = SuperGroup.objects.values('super_group').distinct()
    return render(request, 'base.html', {'super_groups': super_groups, 'new_recs': new_recs})

def get_cpt_groups(request, super_group):
    cpt_groups = SuperGroup.objects.filter(super_group=super_group)
    return render(request, 'cpt_groups.html', {'groups': cpt_groups})

def upload_group_file(request):
    if request.method == 'POST':
        created_count = 0
        data_file = request.FILES['file']
        group_data = data_file.read().decode("utf-8")

        for data_row in group_data.split('\r')[1:]:
            fields = data_row.split(',')
            obj, created = SuperGroup.objects.get_or_create(super_group=fields[1], primary_cpt_group=fields[2])
            if created == True:
                created_count += 1
    
    if created_count > 0:
        s3.save_file(settings.AWS_S3_BUCKET, 'SuperGroups/' + data_file.name, data_file.read())

    return index(request, new_recs=created_count)