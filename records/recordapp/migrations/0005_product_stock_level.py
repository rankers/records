# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordapp', '0004_auto_20150131_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock_level',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
    ]
