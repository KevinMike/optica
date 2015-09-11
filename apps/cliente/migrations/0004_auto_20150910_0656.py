# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20150910_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=45),
        ),
    ]
