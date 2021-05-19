from django.db import models
from . import card_models
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
        return f"({self.infinitive_de}, {self.mood}, {self.tense}, {self.subject}): {self.word_de}"

    class Meta:
        unique_together = ("infinitive_de", "mood", "tense", "subject") # every verb conjugation has an infinitive, a grammatical mood, a temporal-tense, and a subject that's conjugating it.


class Noun(POS):
    word_de_pl = models.CharField(max_length=20)
    word_en_pl = models.CharField(max_length=20, default="temporary")
    pluralization_model = models.CharField(max_length=20) # TODO change to Integer choice
    gender = models.CharField(max_length=1) # # TODO change to Integer choice: M, F, N
    
    @classmethod
    def create(cls, **kwargs):
        noun = cls.objects.create(**kwargs)
        card_models.NounGenderGuess_Card.objects.create(pos=noun)
        card_models.NounPluralizationGuess_Card.objects.create(pos=noun)

    def __str__(self):
        gender_dic = {"M": "der", "F": "die", "N": "das", "P": "die"}
        return f"{gender_dic[self.gender]} {self.word_de} (die {self.word_de_pl})"


class Decliner(POS):
    case = models.CharField(max_length=3) # TODO change to Integer choice: Nom, Akk, Dat, Gen

    class Meta:
        abstract=True


class PersonalPronoun(Decliner):
    plural_order = models.CharField(max_length=10) # TODO change to Integer choice (ich, du, er, sie, es, wir, ihr, sie, Sie)
    person_order = models.IntegerField() # 1st person, 2nd person, 3rd person
    case = models.CharField(max_length=3)

    @classmethod
    def create(cls, **kwargs):
        personal_pronoun = cls.objects.create(**kwargs)
        card_models.PersonalPronoun_Card.objects.create(pos=personal_pronoun)

    def __str__(self):
        return f"({self.word_en}, {self.case}): {self.word_de}"
    
    class Meta:
        # https://en.wikipedia.org/wiki/German_pronouns#Personal_pronouns
        unique_together = ("plural_order", "person_order", "case", "word_en")


class Article(Decliner):
    gender = models.CharField(max_length=1) # TODO change to Integer choice: M, F, N
    definite = models.BooleanField() # definite or indefinite

    def __str__(self):
        return f"({self.gender}, {self.case}, {self.definite}): {self.word_de}"

    class Meta:
        unique_together = ("case", "gender", "definite")
