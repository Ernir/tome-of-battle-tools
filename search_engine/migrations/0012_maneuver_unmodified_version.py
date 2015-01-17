# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0011_discipline_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='maneuver',
            name='unmodified_version',
            field=models.ForeignKey(blank=True, null=True, to='search_engine.Maneuver'),
            preserve_default=True,
        ),
    ]
