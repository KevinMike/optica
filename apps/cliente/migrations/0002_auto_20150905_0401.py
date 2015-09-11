# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'CLIENTES'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='foto',
            field=models.FileField(default=datetime.datetime(2015, 9, 5, 4, 1, 34, 815995, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
    ]
