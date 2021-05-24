from django.db import models
from . import card_models

# RevLog models
class RevLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True) # the datetime that the review gets added
    duration = models.IntegerField() # the time spent on the flashcard
    rating = models.IntegerField() # the review difficulty logged (1, 2, 3, 4) TODO change to Integer choice

    class Meta:
        abstract=True

    def __str__(self):
        return f"""{self.card.pos}:\n - study_timestamp: {self.timestamp}\n - study_duration: {self.duration}\n - study_rating: {self.rating}"""


class NounGenderGuess_RevLog(RevLog):
    card = models.ForeignKey(
        card_models.NounGenderGuess_Card,
        on_delete=models.SET_NULL,
        null=True,
        related_name="revlogs") # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)


class NounPluralizationGuess_RevLog(RevLog):
    card = models.ForeignKey(
        card_models.NounPluralizationGuess_Card,
        on_delete=models.SET_NULL,
        null=True,
        related_name="revlogs") # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)


class NounEnDeMeaning_RevLog(RevLog):
    card = models.ForeignKey(
        card_models.NounEnDeMeaning_Card,
        on_delete=models.SET_NULL,
        null=True,
        related_name="revlogs") # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)


class NounDeEnMeaning_RevLog(RevLog):
    card = models.ForeignKey(
        card_models.NounDeEnMeaning_Card,
        on_delete=models.SET_NULL,
        null=True,
        related_name="revlogs") # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)


class PersonalPronoun_RevLog(RevLog):
    card = models.ForeignKey(
        card_models.PersonalPronoun_Card,
        on_delete=models.SET_NULL,
        null=True,
        related_name="revlogs") # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)

class Article_RevLog(RevLog):
    card = models.ForeignKey(
        card_models.Article_Card,
        on_delete=models.SET_NULL,
        null=True,
        related_name="revlogs") # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)
