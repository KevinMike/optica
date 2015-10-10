# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0003_auto_20150922_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='dni_cliente',
            field=models.ForeignKey(blank=True, to='cliente.Cliente', null=True),
        ),
    ]
