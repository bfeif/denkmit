# Generated by Django 3.2 on 2021-05-03 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0015_auto_20210503_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalpronoun',
            name='person',
            field=models.IntegerField(default=0),
        ),
    ]
