# Generated by Django 3.2 on 2021-05-01 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb_de', models.CharField(max_length=20)),
                ('verb_en', models.CharField(max_length=20)),
                ('tense', models.CharField(max_length=10)),
                ('mood', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=10)),
                ('valency', models.IntegerField()),
            ],
        ),
    ]