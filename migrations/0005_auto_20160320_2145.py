# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-20 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]
