# Generated by Django 3.2 on 2021-05-02 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0010_auto_20210502_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='added_timestamp',
        ),
        migrations.RemoveField(
            model_name='noun',
            name='added_timestamp',
        ),
        migrations.RemoveField(
            model_name='personalpronoun',
            name='added_timestamp',
        ),
        migrations.RemoveField(
            model_name='verb',
            name='added_timestamp',
        ),
    ]
