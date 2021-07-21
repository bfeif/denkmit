# Generated by Django 3.2 on 2021-07-21 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0035_preposition'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrepositionDeclination_Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_suspended', models.BooleanField(default=False)),
                ('last_studied_date', models.DateField(auto_now_add=True)),
                ('num_repetitions', models.IntegerField(default=0)),
                ('ease', models.FloatField(default=1.0)),
                ('interval', models.FloatField(default=0.25)),
                ('pos', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='flashcards.preposition')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
