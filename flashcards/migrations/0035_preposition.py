# Generated by Django 3.2 on 2021-07-21 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0034_auto_20210527_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_de', models.CharField(max_length=110)),
                ('word_en', models.CharField(max_length=110)),
                ('case', models.CharField(max_length=3)),
            ],
            options={
                'unique_together': {('word_de', 'word_en')},
            },
        ),
    ]
