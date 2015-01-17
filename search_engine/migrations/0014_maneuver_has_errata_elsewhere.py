# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0013_auto_20150116_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='maneuver',
            name='has_errata_elsewhere',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
