# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blink_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='IMDb_id',
            new_name='imbd_id',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='IMDB_url',
            new_name='imdb_url',
        ),
    ]
