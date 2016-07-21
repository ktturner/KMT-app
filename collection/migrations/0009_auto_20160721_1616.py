# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 16:16
from __future__ import unicode_literals

import collection.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0008_item_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=collection.models.image_path),
        ),
    ]
