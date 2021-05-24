# Generated by Django 3.2 on 2021-05-24 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0030_auto_20210524_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='NounEnDeMeaning_RevLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='revlogs', to='flashcards.nounendemeaning_card')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NounDeEnMeaning_RevLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='revlogs', to='flashcards.noundeenmeaning_card')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
