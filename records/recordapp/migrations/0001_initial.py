# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('cost', models.DecimalField(max_digits=7, decimal_places=2)),
                ('retail_price', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SoldItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sale_price', models.DecimalField(max_digits=7, decimal_places=2)),
                ('shipping_cost', models.DecimalField(max_digits=7, decimal_places=2)),
                ('platform', models.ForeignKey(to='recordapp.Platform')),
                ('product', models.ForeignKey(to='recordapp.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
