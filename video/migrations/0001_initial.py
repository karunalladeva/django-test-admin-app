# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-29 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=256)),
                ('lname', models.CharField(max_length=256)),
                ('mobile', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('length', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
            ],
        ),
    ]
