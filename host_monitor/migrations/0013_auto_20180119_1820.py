# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-19 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host_monitor', '0012_host_pod_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='pod_count',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='容器数量'),
        ),
    ]
