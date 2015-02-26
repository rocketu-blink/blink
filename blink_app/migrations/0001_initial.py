# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('imdb_id', models.CharField(max_length=30, null=True)),
                ('imdb_url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('release_year', models.IntegerField()),
                ('runtime', models.IntegerField()),
                ('mpaa_rating', models.CharField(max_length=10)),
                ('budget', models.IntegerField()),
                ('revenue', models.IntegerField()),
                ('synopsis', models.TextField()),
                ('imdb_rating', models.FloatField(null=True)),
                ('poster', models.URLField()),
                ('IMDb_id', models.CharField(max_length=30, null=True)),
                ('IMDB_url', models.URLField()),
                ('netflix_url', models.URLField()),
                ('hulu_url', models.URLField()),
                ('prime_url', models.URLField()),
                ('characters', models.ManyToManyField(to='blink_app.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('imdb_id', models.CharField(max_length=30, null=True)),
                ('imdb_url', models.URLField()),
                ('headshot', models.URLField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SourceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='type',
            field=models.ManyToManyField(to='blink_app.PersonType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(to='blink_app.ContentType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='content',
            name='director',
            field=models.ManyToManyField(related_name='director', to='blink_app.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='content',
            name='genre',
            field=models.ManyToManyField(to='blink_app.Genre'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='content',
            name='keywords',
            field=models.ManyToManyField(to='blink_app.Keyword'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='content',
            name='source_types',
            field=models.ManyToManyField(to='blink_app.SourceType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='content',
            name='writer',
            field=models.ManyToManyField(related_name='writer', to='blink_app.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='actor',
            field=models.ManyToManyField(to='blink_app.Person'),
            preserve_default=True,
        ),
    ]
