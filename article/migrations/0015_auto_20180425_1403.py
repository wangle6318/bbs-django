# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-25 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20180425_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimg',
            name='carousel',
            field=models.ImageField(unique=True, upload_to='carousel/', verbose_name='轮播图'),
        ),
    ]