# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-10 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20160827_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='get_image_filename', verbose_name='圖片')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='商品')),
            ],
        ),
    ]