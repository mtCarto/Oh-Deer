# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('animal_type', models.CharField(max_length=12, choices=[(b'DEER', b'Deer'), (b'RACC', b'Raccoon'), (b'RAB', b'Rabbit'), (b'SCAT', b'Scat')])),
                ('num_animal', models.SmallIntegerField(default=1)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('sighting_date', models.DateTimeField()),
                ('additional_info', models.TextField(max_length=300, null=True, blank=True)),
                ('points', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
