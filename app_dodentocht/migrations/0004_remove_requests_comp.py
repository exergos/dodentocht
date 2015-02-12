# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_dodentocht', '0003_requests_comp_requested'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='comp',
        ),
    ]
