# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0004_auto_20150902_0533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name_plural': 'PRODUCTOS'},
        ),
        migrations.AddField(
            model_name='proveedor',
            name='observaciones',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_sugerido',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock_minimo',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
