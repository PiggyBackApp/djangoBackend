# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 08:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20170418_0350'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmedRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passengers', models.IntegerField(blank=True, null=True)),
                ('request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmed_requests', to='posts.Post')),
            ],
        ),
        migrations.RemoveField(
            model_name='request',
            name='driver_post',
        ),
    ]