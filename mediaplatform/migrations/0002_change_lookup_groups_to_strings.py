# Generated by Django 2.0.7 on 2018-07-20 12:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediaplatform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='lookup_groups',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=[], size=None),
        ),
    ]
