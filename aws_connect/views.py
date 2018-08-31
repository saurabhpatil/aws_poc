from django.shortcuts import render
from django.http import HttpResponse
from aws_connect.models import SuperGroup

def index(request):
    super_groups = SuperGroup.objects.values('super_group').distinct()
    return render(request, 'base.html', {'super_groups': super_groups})

def get_cpt_groups(request, super_group):
    cpt_groups = SuperGroup.objects.filter(super_group=super_group)
    return render(request, 'cpt_groups.html', {'groups': cpt_groups})