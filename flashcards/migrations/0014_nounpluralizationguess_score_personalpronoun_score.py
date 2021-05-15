# Generated by Django 3.2 on 2021-05-14 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0013_rename_noungenderscore_noungenderguess_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalPronoun_Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_studied_utc', models.DateTimeField(auto_now_add=True)),
                ('ease', models.FloatField(default=1.0)),
                ('interval', models.FloatField(default=0.25)),
                ('pos', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flashcards.personalpronoun')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NounPluralizationGuess_Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_studied_utc', models.DateTimeField(auto_now_add=True)),
                ('ease', models.FloatField(default=1.0)),
                ('interval', models.FloatField(default=0.25)),
                ('pos', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flashcards.noun')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]