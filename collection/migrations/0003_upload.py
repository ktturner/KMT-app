# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 17:55
from __future__ import unicode_literals

import collection.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_item_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=collection.models.get_image_path)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to='collection.Item')),
            ],
        ),
    ]
