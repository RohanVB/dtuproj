# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-07 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoPage', '0006_specialisation_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_name',
            name='spec1',
            field=models.CharField(default='no_info', max_length=500),
        ),
    ]