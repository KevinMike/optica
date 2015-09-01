# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('almacen', '0001_initial'),
        ('receta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('nro', models.IntegerField(serialize=False, primary_key=True)),
                ('fecha', models.DateField()),
                ('subtotal', models.IntegerField(null=True, blank=True)),
                ('total', models.IntegerField(null=True, blank=True)),
                ('observaciones', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('nro_venta', models.ForeignKey(primary_key=True, serialize=False, to='facturacion.Venta')),
                ('cantidad', models.IntegerField()),
                ('codigo_producto', models.ForeignKey(blank=True, to='almacen.Producto', null=True)),
                ('id_receta', models.ForeignKey(null=True, blank=True, to='receta.Receta', unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='venta',
            name='dni_cliente',
            field=models.ForeignKey(blank=True, to='cliente.Cliente', null=True),
        ),
    ]
