from django.shortcuts import render
from django.http import HttpResponse
from aws_connect.models import SuperGroup

def index(request):
    groups = SuperGroup.objects.filter(super_group='A - Neurostim')
    return render(request, 'base.html', {'cpt_groups': groups})

def get_cpt_groups(request):
    