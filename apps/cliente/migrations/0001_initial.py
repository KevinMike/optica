# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('dni', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('direccion', models.TextField(null=True, blank=True)),
                ('telefono', models.CharField(max_length=15, null=True, blank=True)),
                ('email', models.CharField(max_length=30, null=True, blank=True)),
                ('fecha_nacimiento', models.DateField(null=True, blank=True)),
                ('ocupacion', models.CharField(max_length=50, null=True, blank=True)),
                ('foto', models.BinaryField(null=True, blank=True)),
            ],
        ),
    ]
