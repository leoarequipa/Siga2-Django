# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_disciplina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='score',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
