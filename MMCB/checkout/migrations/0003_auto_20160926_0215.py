# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20160926_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='number',
            field=models.CharField(max_length=22, verbose_name='訂單編號'),
        ),
    ]