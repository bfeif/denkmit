# Generated by Django 3.2 on 2021-07-25 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0037_prepositiondeclination_revlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfinitiveVerb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_de', models.CharField(max_length=110)),
                ('word_en', models.CharField(max_length=110)),
                ('word_de_perfekt', models.CharField(max_length=110)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
