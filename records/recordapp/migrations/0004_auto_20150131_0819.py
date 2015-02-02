# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordapp', '0003_auto_20150131_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='incude_shipping_in_transaction_cost',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='platform',
            name='transaction_cost',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
    ]
