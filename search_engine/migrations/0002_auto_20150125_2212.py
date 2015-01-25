# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maneuver',
            name='type',
            field=models.ForeignKey(related_name='maneuvers', null=True, to='search_engine.ManeuverType', blank=True),
            preserve_default=True,
        ),
    ]
