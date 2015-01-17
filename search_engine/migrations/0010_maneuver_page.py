# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0009_auto_20150113_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='maneuver',
            name='page',
            field=models.IntegerField(default=52),
            preserve_default=False,
        ),
    ]
