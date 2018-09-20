# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-12 02:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180912_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, null=True, unique=True, verbose_name='手机号')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='地址')),
            ],
            options={
                'db_table': 'student_info',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='stu_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.StudentInfo'),
        ),
    ]
