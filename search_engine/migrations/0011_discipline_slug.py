# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0010_maneuver_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='discipline',
            name='slug',
            field=models.SlugField(default='Save this again'),
            preserve_default=False,
        ),
    ]
