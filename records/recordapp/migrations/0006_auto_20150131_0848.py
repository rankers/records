# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordapp', '0005_product_stock_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overhead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('date', models.DateTimeField()),
                ('cost', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
