# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recordapp', '0008_auto_20150131_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='solditem',
            name='sold_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 31, 17, 8, 46, 260088, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
