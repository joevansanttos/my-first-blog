# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bicicleta',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('fabricante', models.CharField(max_length=45)),
                ('cor', models.CharField(max_length=20)),
                ('marcha', models.BooleanField(verbose_name='Marcha')),
                ('proprietario', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
