# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock', models.SmallIntegerField(null=True, blank=True)),
                ('observacion', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=30, null=True, blank=True)),
                ('marca', models.CharField(max_length=30, null=True, blank=True)),
                ('color', models.CharField(max_length=20, null=True, blank=True)),
                ('longitud', models.CharField(max_length=15, null=True, blank=True)),
                ('precio_sugerido', models.IntegerField(null=True, blank=True)),
                ('stock_minimo', models.IntegerField(null=True, blank=True)),
                ('id_categoria', models.ForeignKey(blank=True, to='almacen.Categoria', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_producto', models.ForeignKey(to='almacen.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40, null=True, blank=True)),
                ('telefono', models.CharField(max_length=30, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='productoproveedor',
            name='id_proveedor',
            field=models.ForeignKey(to='almacen.Proveedor'),
        ),
        migrations.AddField(
            model_name='almacen',
            name='codigo_producto',
            field=models.ForeignKey(blank=True, to='almacen.Producto', null=True),
        ),
    ]
