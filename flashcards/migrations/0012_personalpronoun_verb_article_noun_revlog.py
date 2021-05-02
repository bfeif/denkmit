# Generated by Django 3.2 on 2021-05-02 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0011_auto_20210502_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='RevLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalPronoun_Verb_Article_Noun',
            fields=[
                ('revlog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='flashcards.revlog')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flashcards.article')),
                ('noun', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flashcards.noun')),
                ('personal_pronoun', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flashcards.personalpronoun')),
                ('verb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flashcards.verb')),
            ],
            bases=('flashcards.revlog',),
        ),
    ]