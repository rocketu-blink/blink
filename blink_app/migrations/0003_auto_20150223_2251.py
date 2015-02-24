# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blink_app', '0002_auto_20150223_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='imbd_id',
            new_name='imdb_id',
        ),
    ]
