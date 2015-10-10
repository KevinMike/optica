# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0002_auto_20150922_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='dni_cliente',
            field=models.ForeignKey(to='cliente.Cliente'),
        ),
    ]
