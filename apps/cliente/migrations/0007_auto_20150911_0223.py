# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_auto_20150911_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(null=True, blank=True),
        ),
    ]
