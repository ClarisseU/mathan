# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-16 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namecat', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('img_name', models.CharField(max_length=60)),
                ('img_description', models.CharField(max_length=60)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mathanapp.Category')),
            ],
        ),
    ]
