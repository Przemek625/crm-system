# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-02 12:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0003_auto_20171101_1724'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customertocompany',
            unique_together=set([('customer', 'company')]),
        ),
    ]
