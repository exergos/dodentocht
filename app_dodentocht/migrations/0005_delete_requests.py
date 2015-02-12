# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_dodentocht', '0004_remove_requests_comp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='requests',
        ),
    ]
