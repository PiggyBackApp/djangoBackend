# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 08:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='travelDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
