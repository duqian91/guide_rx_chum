# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 19:44
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('guide', '0002_auto_20170227_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_img',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image'),
        ),
    ]