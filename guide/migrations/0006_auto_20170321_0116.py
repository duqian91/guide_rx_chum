# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 01:16
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0005_auto_20170321_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='document',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guides', to='filer.File'),
        ),
    ]