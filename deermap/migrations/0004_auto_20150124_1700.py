# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deermap', '0003_auto_20150124_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sighting',
            old_name='animal_typ',
            new_name='animal_type',
        ),
        migrations.RenameField(
            model_name='sighting',
            old_name='sighting_d',
            new_name='sighting_date',
        ),
    ]
