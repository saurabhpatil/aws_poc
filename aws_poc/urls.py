"""aws_poc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import aws_connect.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="main"),
    path('api/cpt-groups/<super_group>', views.get_cpt_groups, name="cpt_groups"),
    path('api/upload/cpt-groups', views.upload_group_file, name="cpt-upload")
]
