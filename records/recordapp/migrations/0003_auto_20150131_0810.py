# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordapp', '0002_product_shipping_charge'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('shipping_charge', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='product',
            name='shipping_charge',
        ),
        migrations.AddField(
            model_name='solditem',
            name='shipping_location',
            field=models.ForeignKey(to='recordapp.ShippingLocation', null=True),
            preserve_default=True,
        ),
    ]
