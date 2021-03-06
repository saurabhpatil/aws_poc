# Generated by Django 2.1 on 2018-09-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws_connect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileHandler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.TextField(max_length=255)),
                ('file_type', models.TextField(max_length=10)),
                ('s3_bucket', models.TextField(max_length=100)),
                ('s3_folder', models.TextField(max_length=100)),
                ('uploaded_at', models.DateTimeField()),
            ],
        ),
    ]
