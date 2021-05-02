# Generated by Django 3.2 on 2021-05-02 01:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0009_alter_personalpronoun_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='added_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 1, 18, 4, 635572)),
        ),
        migrations.AddField(
            model_name='noun',
            name='added_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 1, 18, 4, 603063)),
        ),
        migrations.AddField(
            model_name='personalpronoun',
            name='added_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 1, 18, 4, 635161)),
        ),
        migrations.AddField(
            model_name='verb',
            name='added_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 1, 18, 4, 635953)),
        ),
    ]