# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dodentocht_snelheid',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Rang', models.IntegerField(default=0)),
                ('Naam', models.TextField(default='')),
                ('Start', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Weert', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Bornem', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Wintam', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Ruisbroek', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Breendonk', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Steenhuffel', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Peizegem', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Buggenhout', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Opdorp', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Lippelo', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Puurs', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Oppuurs', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Sint_Amands', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Branst', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Aankomst', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Totaal', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='dodentocht_snelheid_avg',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Start', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Weert', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Bornem', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Wintam', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Ruisbroek', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Breendonk', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Steenhuffel', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Peizegem', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Buggenhout', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Opdorp', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Lippelo', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Puurs', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Oppuurs', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Sint_Amands', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Branst', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Aankomst', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Totaal', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='dodentocht_tijd',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Rang', models.IntegerField(default=0)),
                ('Naam', models.TextField(default='')),
                ('Start', models.DateTimeField()),
                ('Weert', models.DateTimeField()),
                ('Bornem', models.DateTimeField()),
                ('Wintam', models.DateTimeField()),
                ('Ruisbroek', models.DateTimeField()),
                ('Breendonk', models.DateTimeField()),
                ('Steenhuffel', models.DateTimeField()),
                ('Peizegem', models.DateTimeField()),
                ('Buggenhout', models.DateTimeField()),
                ('Opdorp', models.DateTimeField()),
                ('Lippelo', models.DateTimeField()),
                ('Puurs', models.DateTimeField()),
                ('Oppuurs', models.DateTimeField()),
                ('Sint_Amands', models.DateTimeField()),
                ('Branst', models.DateTimeField()),
                ('Aankomst', models.DateTimeField()),
                ('Totaal', models.TextField(default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='dodentocht_totaal_avg',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Data', models.TextField(default='')),
                ('Start', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Weert', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Bornem', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Wintam', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Ruisbroek', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Breendonk', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Steenhuffel', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Peizegem', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Buggenhout', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Opdorp', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Lippelo', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Puurs', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Oppuurs', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Sint_Amands', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Branst', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
                ('Aankomst', models.DecimalField(decimal_places=5, default=0, max_digits=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='requests',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ip_address', models.IPAddressField()),
                ('pub_date', models.DateTimeField()),
                ('name_requested', models.TextField(default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
