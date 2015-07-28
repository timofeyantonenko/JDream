# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0006_auto_20150714_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent',
            name='talent_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
