# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-14 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, unique=True)),
                ('book', models.ManyToManyField(to='app01.Book')),
            ],
        ),
    ]
