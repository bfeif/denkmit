# Generated by Django 3.2 on 2021-05-24 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0027_auto_20210524_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noun',
            name='word_de_pl',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='noun',
            name='word_en_pl',
            field=models.CharField(default='temporary', max_length=40),
        ),
    ]
