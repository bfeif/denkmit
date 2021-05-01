# Generated by Django 3.2 on 2021-05-01 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_de', models.CharField(max_length=3)),
                ('article_en', models.CharField(max_length=10)),
                ('definite', models.BooleanField()),
                ('case', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Noun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noun_de', models.CharField(max_length=20)),
                ('noun_en', models.CharField(max_length=20)),
                ('noun_de_pl', models.CharField(max_length=20)),
                ('pluralization_model', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
    ]
