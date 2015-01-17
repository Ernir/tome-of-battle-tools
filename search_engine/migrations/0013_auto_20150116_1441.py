# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0012_maneuver_unmodified_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maneuver',
            old_name='unmodified_version',
            new_name='alternate_version',
        ),
    ]
