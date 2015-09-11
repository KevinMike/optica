# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20150905_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(default=b'pic_folder/default_user.png', null=True, upload_to=b'pic_folder/', blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
