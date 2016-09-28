# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 17:31
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='number',
            field=models.DecimalField(decimal_places=0, max_digits=20, validators=[django.core.validators.MinValueValidator(0)], verbose_name='訂單編號'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='訂購時間'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='total',
            field=models.PositiveIntegerField(verbose_name='總額'),
        ),
    ]