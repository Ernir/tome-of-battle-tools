# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0004_auto_20150105_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavingThrow',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='maneuver',
            name='saving_throw',
            field=models.ForeignKey(null=True, to='search_engine.SavingThrow', blank=True),
            preserve_default=True,
        ),
    ]
