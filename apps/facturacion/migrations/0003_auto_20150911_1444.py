# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_detalleventa_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateField(null=True, blank=True),
        ),
    ]
