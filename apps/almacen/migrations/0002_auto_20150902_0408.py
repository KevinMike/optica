# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='productos',
            field=models.ManyToManyField(to='almacen.Producto'),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='stock',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
