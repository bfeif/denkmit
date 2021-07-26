# Generated by Django 3.2 on 2021-07-25 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0038_infinitiveverb'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfinitiveVerbDeEnMeaning_Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_suspended', models.BooleanField(default=False)),
                ('last_studied_date', models.DateField(auto_now_add=True)),
                ('num_repetitions', models.IntegerField(default=0)),
                ('ease', models.FloatField(default=1.0)),
                ('interval', models.FloatField(default=0.25)),
                ('pos', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='flashcards.infinitiveverb')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InfinitiveVerbEnDeMeaning_Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_suspended', models.BooleanField(default=False)),
                ('last_studied_date', models.DateField(auto_now_add=True)),
                ('num_repetitions', models.IntegerField(default=0)),
                ('ease', models.FloatField(default=1.0)),
                ('interval', models.FloatField(default=0.25)),
                ('pos', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='flashcards.infinitiveverb')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InfinitiveVerbEnDeMeaning_RevLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revlogs', to='flashcards.infinitiveverbendemeaning_card')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InfinitiveVerbDeEnMeaning_RevLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revlogs', to='flashcards.infinitiveverbdeenmeaning_card')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]