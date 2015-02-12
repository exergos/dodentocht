# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_dodentocht', '0002_requests_comp'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='comp_requested',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
