# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='polygons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prov', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('poly', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='providers_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.BigIntegerField()),
                ('language', models.CharField(max_length=150)),
                ('currency', models.CharField(max_length=100)),
            ],
        ),
    ]