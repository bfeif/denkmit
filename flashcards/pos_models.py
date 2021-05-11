from django.db import models
import time

class POS(models.Model):
    word_de = models.CharField(max_length=20)
    word_en = models.CharField(max_length=20)
    
    class Meta:
        abstract=True


class Verb(POS):
    infinitive_de = models.CharField(max_length=20, default="temporary")
    mood = models.CharField(max_length=10) # TODO change to Integer choice
    tense = models.CharField(max_length=10) # TODO change to Integer choice
    subject = models.CharField(max_length=10) # TODO change to Integer choice (ich, du, er_sie_es, wir, ihr, Sie)
    valency = models.IntegerField() # TODO change to Integer choice as per https://en.wikipedia.org/wiki/Verb#Valency
    # TODO: phrasal verbs and the requisite fields

    def __str__(self):
        return f"({self.infinitive_de}, {self.mood}, {self.tense}, {self.subject}): {self.verb_de}"

    class Meta:
        unique_together = ("infinitive_de", "mood", "tense", "subject") # every verb conjugation has an infinitive, a grammatical mood, a temporal-tense, and a subject that's conjugating it.


class Noun(POS):
    noun_de_pl = models.CharField(max_length=20)
    noun_en_pl = models.CharField(max_length=20, default="temporary")
    pluralization_model = models.CharField(max_length=20) # TODO change to Integer choice
    gender = models.CharField(max_length=1) # # TODO change to Integer choice: M, F, N

    def __str__(self):
        gender_dic = {"M": "der", "F": "die", "N": "das", "P": "die"}
        return f"{gender_dic[self.gender]} {self.noun_de} (die {self.noun_de_pl})"


class PersonalPronoun(POS):
    case = models.CharField(max_length=3) # TODO change to Integer choice: Nom, Akk, Dat, Gen
    nom_pronoun_de = models.CharField(max_length=10, default="temporary") # TODO change to Integer choice (ich, du, er, sie, es, wir, ihr, Sie)
    person = models.IntegerField() # 1st person, 2nd person, 3rd person
    is_plural = models.BooleanField(default=False)

    def __str__(self):
        return f"({self.nom_pronoun_de}, {self.case}): {self.pronoun_de}"
    
    class Meta:
        unique_together = ("nom_pronoun_de", "case", "person", "is_plural")


class Article(POS):
    case = models.CharField(max_length=3) # TODO change to Integer choice: Nom, Akk, Dat, Gen
    gender = models.CharField(max_length=1) # TODO change to Integer choice: M, F, N
    definite = models.BooleanField() # definite or indefinite

    def __str__(self):
        return f"({self.gender}, {self.case}, {self.definite}): {self.article_de}"

    class Meta:
        unique_together = ("case", "gender", "definite")
