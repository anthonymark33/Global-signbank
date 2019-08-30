# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-03 12:12
from __future__ import unicode_literals

from django.db import migrations, models
import signbank.video.models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20170323_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossvideo',
            name='videofile',
            field=models.FileField(storage=signbank.video.models.GlossVideoStorage(), upload_to=signbank.video.models.get_video_file_path, verbose_name='video file'),
        ),
    ]
