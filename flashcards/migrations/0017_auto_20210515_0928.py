# Generated by Django 3.2 on 2021-05-15 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0016_auto_20210515_0845'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NounGenderGuess_Score',
            new_name='NounGenderGuess_Card',
        ),
        migrations.RenameModel(
            old_name='NounPluralizationGuess_Score',
            new_name='NounPluralizationGuess_Card',
        ),
        migrations.RenameModel(
            old_name='PersonalPronoun_Score',
            new_name='PersonalPronoun_Card',
        ),
    ]
