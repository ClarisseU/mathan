# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-03 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathanapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='price',
            field=models.CharField(max_length=60, null=True),
        ),
    ]