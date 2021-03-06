# Generated by Django 3.2 on 2021-05-14 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0014_nounpluralizationguess_score_personalpronoun_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noungenderguess_revlog',
            name='pos',
        ),
        migrations.RemoveField(
            model_name='nounpluralizationguess_revlog',
            name='pos',
        ),
        migrations.RemoveField(
            model_name='personalpronoun_revlog',
            name='pos',
        ),
        migrations.AddField(
            model_name='noungenderguess_revlog',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flashcards.noungenderguess_score'),
        ),
        migrations.AddField(
            model_name='noungenderguess_score',
            name='num_repetitions',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='nounpluralizationguess_revlog',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flashcards.nounpluralizationguess_score'),
        ),
        migrations.AddField(
            model_name='nounpluralizationguess_score',
            name='num_repetitions',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personalpronoun_revlog',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flashcards.personalpronoun_score'),
        ),
        migrations.AddField(
            model_name='personalpronoun_score',
            name='num_repetitions',
            field=models.IntegerField(default=0),
        ),
    ]
