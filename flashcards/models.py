from django.db import models

class Noun(models.Model):
    noun_de = models.CharField(max_length=20)
    noun_en = models.CharField(max_length=20)
    noun_de_pl = models.CharField(max_length=20)
    noun_en_pl = models.CharField(max_length=20, default="temp")
    pluralization_model = models.CharField(max_length=20) # TODO change to Integer choice
    gender = models.CharField(max_length=1) # # TODO change to Integer choice: M, F, N

class PersonalPronoun(models.Model):
    pronoun_de = models.CharField(max_length=20)
    pronoun_en = models.CharField(max_length=20)
    case = models.CharField(max_length=3) # TODO change to Integer choice: Nom, Akk, Dat, Gen
    nom_pronoun_de = models.CharField(max_length=10, default="temp") # TODO change to Integer choice (ich, du, er, sie, es, wir, ihr, Sie)
    order = models.CharField(max_length=10, default="temp") # TODO change to Integer choice (ich, du, er_sie_es, wir, ihr, Sie)

class Article(models.Model):
    article_de = models.CharField(max_length=3) # the article in german
    article_en = models.CharField(max_length=10) # the article in german english
    definite = models.BooleanField() # definite or indefinite
    case = models.CharField(max_length=3) # TODO change to Integer choice: Nom, Akk, Dat, Gen
    gender = models.CharField(max_length=1) # TODO change to Integer choice: M, F, N

class Verb(models.Model):
    verb_de = models.CharField(max_length=20)
    verb_en = models.CharField(max_length=20)
    tense = models.CharField(max_length=10) # TODO change to Integer choice
    mood = models.CharField(max_length=10) # TODO change to Integer choice
    subject = models.CharField(max_length=10) # TODO change to Integer choice (ich, du, er_sie_es, wir, ihr, Sie)
    valency = models.IntegerField() # TODO change to Integer choice as per https://en.wikipedia.org/wiki/Verb#Valency
    # TODO: phrasal verbs and the requisite fields