# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maneuver',
            name='classes',
        ),
        migrations.AddField(
            model_name='initiatorclass',
            name='disciplines',
            field=models.ManyToManyField(to='search_engine.Discipline'),
            preserve_default=True,
        ),
    ]
