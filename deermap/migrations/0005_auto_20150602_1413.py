# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('deermap', '0004_auto_20150124_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='additional',
            field=models.CharField(max_length=254, verbose_name=b'Additional Information', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sighting',
            name='animal_type',
            field=models.CharField(max_length=50, verbose_name=b'What kind of animal did you see?', choices=[(b'Deer', b'Deer'), (b'Raccoon', b'Raccoon'), (b'Hare', b'Rabbit'), (b'Rodent', b'Squirrel, Chipmunk, Rat')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sighting',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPointField(srid=4326, verbose_name=b'Location'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sighting',
            name='num_animal',
            field=models.IntegerField(verbose_name=b'How many did you see?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sighting',
            name='sighting_date',
            field=models.DateTimeField(verbose_name=b'Date of the sighting'),
            preserve_default=True,
        ),
    ]
