# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blink_app', '0003_auto_20150223_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(to='blink_app.ContentType', null=True),
            preserve_default=True,
        ),
    ]
