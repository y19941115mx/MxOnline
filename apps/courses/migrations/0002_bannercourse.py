# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-11 13:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name_plural': '轮播课程',
                'proxy': True,
                'verbose_name': '轮播课程',
            },
            bases=('courses.course',),
        ),
    ]
