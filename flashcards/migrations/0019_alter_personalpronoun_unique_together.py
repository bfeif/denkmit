# Generated by Django 3.2 on 2021-05-04 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0018_auto_20210504_2001'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='personalpronoun',
            unique_together={('nom_pronoun_de', 'case', 'person', 'is_plural')},
        ),
    ]
