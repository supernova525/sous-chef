# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 20:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_auto_20160728_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='author',
        ),
        migrations.RemoveField(
            model_name='note',
            name='member',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
