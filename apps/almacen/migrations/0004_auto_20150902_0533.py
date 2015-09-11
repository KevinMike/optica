# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0003_auto_20150902_0515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='almacen',
            name='codigo_producto',
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name_plural': 'CATEGORIAS'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name_plural': 'PRODUCTOS REGISTRADOS'},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'verbose_name_plural': 'PROVEEDORES'},
        ),
        migrations.AddField(
            model_name='producto',
            name='stock_actual',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Almacen',
        ),
    ]
