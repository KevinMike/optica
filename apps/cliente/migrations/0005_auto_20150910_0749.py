# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_auto_20150910_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(default=b'pic_folder/default_user.png', upload_to=b'pic_folder/', blank=True),
        ),
    ]
