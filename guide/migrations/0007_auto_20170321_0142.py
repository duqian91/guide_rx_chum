# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 01:42
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0006_auto_20170321_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_img',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='img', to='filer.File'),
        ),
    ]
