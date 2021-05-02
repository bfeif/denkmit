from django.db import models


# POS models
class Noun(models.Model):
    noun_de = models.CharField(max_length=20)
    noun_en = models.CharField(max_length=20)
    noun_de_pl = models.CharField(max_length=20)
    noun_en_pl = models.CharField(max_length=20, default="temp")
    pluralization_model = models.CharField(max_length=20) # TODO change to Integer choice
    gender = models.CharField(max_length=1) # # TODO change to Integer choice: M, F, N

    def __str__(self):
        gender_dic = {"M": "der", "F": "die", "N": "das", "P": "die"}
        return f"{gender_dic[self.gender]} {self.noun_de} (die {self.noun_de_pl}) "


class PersonalPronoun(models.Model):
    pronoun_de = models.CharField(max_length=20)
    pronoun_en = models.CharField(max_length=20)
    case = models.CharField(max_length=3) # TODO change to Integer choice: Nom, Akk, Dat, Gen
    nom_pronoun_de = models.CharField(max_length=10, default="temp") # TODO change to Integer choice (ich, du, er, sie, es, wir, ihr, Sie)
    order = models.CharField(max_length=10, default="temp") # TODO change to Integer choice (ich, du, er_sie_es, wir, ihr, Sie)

    def __str__(self):
        return f"({self.nom_pronoun_de}, {self.case}): {self.pronoun_de}"
    
    class Meta:
        unique_together = ("nom_pronoun_de", "case")


class Article(models.Model):
    article_de = models.CharField(max_length=10) # the article in german
    article_en = models.CharField(max_length=10) # the article in german english
    case = models.CharField(max_length=3) # TODO change to Integer choice: Nom, Akk, Dat, Gen
    gender = models.CharField(max_length=1) # TODO change to Integer choice: M, F, N
    definite = models.BooleanField() # definite or indefinite

    def __str__(self):
        return f"({self.gender}, {self.case}, {self.definite}): {self.article_de}"

    class Meta:
        unique_together = ("case", "gender", "definite")


class Verb(models.Model):
    verb_de = models.CharField(max_length=20)
    verb_en = models.CharField(max_length=20)
    infinitive_de = models.CharField(max_length=20, default="temp")
    mood = models.CharField(max_length=10) # TODO change to Integer choice
    tense = models.CharField(max_length=10) # TODO change to Integer choice
    subject = models.CharField(max_length=10) # TODO change to Integer choice (ich, du, er_sie_es, wir, ihr, Sie)
    valency = models.IntegerField() # TODO change to Integer choice as per https://en.wikipedia.org/wiki/Verb#Valency
    # TODO: phrasal verbs and the requisite fields

    def __str__(self):
        return f"({self.infinitive_de}, {self.mood}, {self.tense}, {self.subject}): {self.verb_de}"

    class Meta:
        unique_together = ("infinitive_de", "mood", "tense", "subject") # every verb conjugation has an infinitive, a grammatical mood, a temporal-tense, and a subject that's conjugating it.


# RevLog models
class RevLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True) # the datetime that the review gets added
    duration = models.IntegerField() # the time spent on the flashcard
    rating = models.IntegerField() # the review difficulty logged (1, 2, 3, 4) TODO change to Integer choice


class PersonalPronoun_Verb_Article_Noun(RevLog):
    personal_pronoun = models.ForeignKey('PersonalPronoun', on_delete=models.SET_NULL, null=True) # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)
    verb = models.ForeignKey('Verb', on_delete=models.SET_NULL, null=True) # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)
    article = models.ForeignKey('Article', on_delete=models.SET_NULL, null=True) # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)
    noun = models.ForeignKey('Noun', on_delete=models.SET_NULL, null=True) # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)