# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Subject', models.CharField(max_length=250)),
                ('Message', models.CharField(max_length=2000)),
                ('Time', models.DateField()),
            ],
        ),
    ]
