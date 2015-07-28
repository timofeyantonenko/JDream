# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments_text', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd1\x8f')),
                ('comments_likes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Talent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('talent_title', models.CharField(max_length=200)),
                ('talent_text', models.TextField(null=True, blank=True)),
                ('talent_date', models.DateTimeField()),
                ('talent_likes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'talent',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_talent',
            field=models.ForeignKey(to='talent.Talent'),
        ),
    ]
