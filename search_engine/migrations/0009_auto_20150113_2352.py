# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0008_auto_20150109_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maneuver',
            name='discipline',
            field=models.ForeignKey(related_name='disciplines', to='search_engine.Discipline'),
            preserve_default=True,
        ),
    ]
