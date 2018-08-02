# Generated by Django 2.0.7 on 2018-07-13 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mediaplatform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigIntegerField(editable=False, help_text='Legacy SMS collection id', primary_key=True, serialize=False)),
                ('last_updated_at', models.DateTimeField(editable=False, help_text='Last updated at time from SMS', null=True)),
                ('collection', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sms', to='mediaplatform.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('id', models.BigIntegerField(editable=False, help_text='Legacy SMS media id', primary_key=True, serialize=False)),
                ('last_updated_at', models.DateTimeField(editable=False, help_text='Last updated at time from SMS', null=True)),
                ('item', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sms', to='mediaplatform.MediaItem')),
            ],
        ),
    ]