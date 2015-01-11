# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brainstormer', '0002_idea_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='name',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
