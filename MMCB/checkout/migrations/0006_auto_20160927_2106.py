# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-27 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_purchaseorder_order_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(choices=[('UP', '待付款/匯款'), ('PA', '通知已付款'), ('PC', '確認已付款'), ('WS', '商品準備中'), ('SN', '商品已寄出'), ('AB', '放棄此訂單'), ('CA', '取消放棄此訂單'), ('AC', '待賣家確認放棄'), ('AD', '已放棄')], default='UP', max_length=2),
        ),
    ]