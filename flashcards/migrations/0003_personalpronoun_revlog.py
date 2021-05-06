# Generated by Django 3.2 on 2021-05-06 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0002_auto_20210506_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalPronoun_RevLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('personal_pronoun', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flashcards.noun')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
