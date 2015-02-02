# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recordapp', '0007_overhead_overhead_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='overhead',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 31, 17, 4, 58, 961165, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platform',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 31, 17, 5, 9, 928105, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 31, 17, 5, 12, 712256, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippinglocation',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 31, 17, 5, 17, 760149, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solditem',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 31, 17, 5, 21, 967594, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
