# Generated by Django 3.2 on 2021-05-14 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0008_auto_20210511_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalPronoun_RevLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('pos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flashcards.personalpronoun')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
