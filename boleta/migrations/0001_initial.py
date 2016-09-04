# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ingresoboletas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('total', models.IntegerField()),
                ('vendedor', models.IntegerField()),
            ],
        ),
    ]
