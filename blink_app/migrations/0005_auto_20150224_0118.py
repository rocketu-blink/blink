# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blink_app', '0004_auto_20150223_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='budget',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='content',
            name='revenue',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
