# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0002_auto_20150105_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='maneuver',
            name='area',
            field=models.ForeignKey(to='search_engine.Area', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='maneuver',
            name='descriptor',
            field=models.ManyToManyField(to='search_engine.Descriptor', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='maneuver',
            name='effect',
            field=models.ForeignKey(to='search_engine.Effect', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='maneuver',
            name='target',
            field=models.ForeignKey(to='search_engine.Target', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='maneuver',
            name='type',
            field=models.ForeignKey(to='search_engine.ManeuverType', blank=True, default=None),
            preserve_default=False,
        ),
    ]
