# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0005_auto_20150714_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_from',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='comments_talent',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
