# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('deermap', '0002_auto_20150124_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPointField(srid=4326),
            preserve_default=True,
        ),
    ]
