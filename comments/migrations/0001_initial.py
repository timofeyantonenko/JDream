# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('talent', '0006_auto_20150714_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments_text', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd1\x8f')),
                ('comments_likes', models.IntegerField(default=0)),
                ('comments_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comments_from', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
                ('comments_talent', models.ForeignKey(to='talent.Talent')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
