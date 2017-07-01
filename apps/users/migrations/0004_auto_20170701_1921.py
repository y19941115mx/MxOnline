# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-01 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170610_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '修改密码'), ('update_email', '修改邮箱')], max_length=18, verbose_name='验证码类型'),
        ),
    ]
