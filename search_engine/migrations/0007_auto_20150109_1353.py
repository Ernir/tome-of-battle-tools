# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0006_auto_20150106_1606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maneuver',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='maneuver',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
