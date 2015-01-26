# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0002_auto_20150125_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maneuver',
            name='type',
            field=models.ForeignKey(to='search_engine.ManeuverType', related_name='maneuvers', default=5),
            preserve_default=False,
        ),
    ]
