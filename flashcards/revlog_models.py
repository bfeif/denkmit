from django.db import models
from .pos_models import *
from . import card_scores
import time

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
        card_scores.NounGenderGuess_Score,
        on_delete=models.SET_NULL,
        null=True,
        related_name="revlogs") # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)


class NounPluralizationGuess_RevLog(RevLog):
    card = models.ForeignKey(
        card_scores.NounPluralizationGuess_Score,
        on_delete=models.SET_NULL,
        null=True,
        related_name="revlogs") # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)


class PersonalPronoun_RevLog(RevLog):
    card = models.ForeignKey(
        card_scores.PersonalPronoun_Score,
        on_delete=models.SET_NULL,
        null=True,
        related_name="revlogs") # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)
