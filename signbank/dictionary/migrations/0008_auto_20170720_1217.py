# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-20 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0007_auto_20170707_1349'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Language',
            new_name='SignLanguage',
        ),
        migrations.AlterModelOptions(
            name='dialect',
            options={'ordering': ['signlanguage', 'name']},
        ),
        migrations.RenameField(
            model_name='dialect',
            old_name='language',
            new_name='signlanguage',
        ),
        migrations.RenameField(
            model_name='gloss',
            old_name='language',
            new_name='signlanguage',
        ),
    ]