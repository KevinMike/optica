# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0002_auto_20150902_0408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productoproveedor',
            name='codigo_producto',
        ),
        migrations.RemoveField(
            model_name='productoproveedor',
            name='id_proveedor',
        ),
        migrations.AlterModelOptions(
            name='almacen',
            options={'verbose_name_plural': 'Stock de Productos'},
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name_plural': 'Categorias Registradas'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name_plural': 'Productos Registrados'},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'verbose_name_plural': 'Proveedores Registrados'},
        ),
        migrations.RemoveField(
            model_name='producto',
            name='id_categoria',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(blank=True, to='almacen.Categoria', null=True),
        ),
        migrations.DeleteModel(
            name='ProductoProveedor',
        ),
    ]
