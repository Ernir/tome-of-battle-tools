# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0003_auto_20150105_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maneuver',
            name='area',
            field=models.ForeignKey(to='search_engine.Area', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='maneuver',
            name='descriptor',
            field=models.ManyToManyField(null=True, to='search_engine.Descriptor', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='maneuver',
            name='effect',
            field=models.ForeignKey(to='search_engine.Effect', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='maneuver',
            name='target',
            field=models.ForeignKey(to='search_engine.Target', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='maneuver',
            name='type',
            field=models.ForeignKey(to='search_engine.ManeuverType', blank=True, null=True),
            preserve_default=True,
        ),
    ]
