# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0003_auto_20150725_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(related_name='userProfile', null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
