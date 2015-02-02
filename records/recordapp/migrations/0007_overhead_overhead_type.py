# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordapp', '0006_auto_20150131_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='overhead',
            name='overhead_type',
            field=models.CharField(default=b'PR', max_length=2, choices=[(b'BU', b'Business'), (b'PR', b'Product')]),
            preserve_default=True,
        ),
    ]
