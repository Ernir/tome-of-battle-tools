# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0005_auto_20150105_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maneuver',
            name='duration',
            field=models.ForeignKey(blank=True, null=True, to='search_engine.Duration'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='maneuver',
            name='requirements',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
