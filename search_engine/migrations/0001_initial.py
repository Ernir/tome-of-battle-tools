# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Descriptor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('is_timed', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InitiatorClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('disciplines', models.ManyToManyField(related_name='initiator_classes', to='search_engine.Discipline')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Maneuver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('level', models.IntegerField()),
                ('requirements', models.IntegerField(default=0)),
                ('descriptive_text', models.TextField()),
                ('slug', models.SlugField()),
                ('html_description', models.TextField()),
                ('page', models.IntegerField()),
                ('has_errata_elsewhere', models.BooleanField(default=False)),
                ('action', models.ForeignKey(to='search_engine.Action')),
                ('alternate_version', models.ForeignKey(to='search_engine.Maneuver', blank=True, null=True)),
                ('area', models.ForeignKey(to='search_engine.Area', blank=True, null=True)),
                ('descriptor', models.ManyToManyField(null=True, to='search_engine.Descriptor', blank=True)),
                ('discipline', models.ForeignKey(related_name='maneuvers', to='search_engine.Discipline')),
                ('duration', models.ForeignKey(to='search_engine.Duration', blank=True, null=True)),
                ('effect', models.ForeignKey(to='search_engine.Effect', blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ManeuverType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('is_numeric', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SavingThrow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='maneuver',
            name='range',
            field=models.ForeignKey(to='search_engine.Range'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='maneuver',
            name='saving_throw',
            field=models.ForeignKey(to='search_engine.SavingThrow', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='maneuver',
            name='target',
            field=models.ForeignKey(to='search_engine.Target', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='maneuver',
            name='type',
            field=models.ForeignKey(to='search_engine.ManeuverType', blank=True, null=True),
            preserve_default=True,
        ),
    ]
