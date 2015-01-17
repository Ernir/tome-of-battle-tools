# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0007_auto_20150109_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='maneuver',
            name='html_description',
            field=models.TextField(default='Todo: Save this again.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='initiatorclass',
            name='disciplines',
            field=models.ManyToManyField(related_name='initiator_classes', to='search_engine.Discipline'),
            preserve_default=True,
        ),
    ]
