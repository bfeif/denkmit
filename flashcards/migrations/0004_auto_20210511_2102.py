# Generated by Django 3.2 on 2021-05-11 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0003_personalpronoun_revlog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_de',
            new_name='word_de',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_en',
            new_name='word_en',
        ),
        migrations.RenameField(
            model_name='noun',
            old_name='noun_de',
            new_name='word_de',
        ),
        migrations.RenameField(
            model_name='noun',
            old_name='noun_en',
            new_name='word_en',
        ),
        migrations.RenameField(
            model_name='personalpronoun',
            old_name='pronoun_de',
            new_name='word_de',
        ),
        migrations.RenameField(
            model_name='personalpronoun',
            old_name='pronoun_en',
            new_name='word_en',
        ),
        migrations.RenameField(
            model_name='verb',
            old_name='verb_de',
            new_name='word_de',
        ),
        migrations.RenameField(
            model_name='verb',
            old_name='verb_en',
            new_name='word_en',
        ),
    ]
