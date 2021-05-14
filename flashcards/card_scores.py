from django.db import models
from . import pos_models
from . import card_defaults

class CardScore(models.Model):
    last_studied_utc = models.DateTimeField(auto_now_add=True)
    ease = models.FloatField(default=card_defaults.EASE_INIT)
    interval = models.FloatField(default=card_defaults.INTERVAL_INIT)

    class Meta:
        abstract=True


class NounGenderGuess_Score(CardScore):
    pos = models.OneToOneField(pos_models.Noun, on_delete=models.SET_NULL, null=True)


class NounPluralizationGuess_Score(CardScore):
    pos = models.OneToOneField(pos_models.Noun, on_delete=models.SET_NULL, null=True)


class PersonalPronoun_Score(CardScore):
    pos = models.OneToOneField(pos_models.PersonalPronoun, on_delete=models.SET_NULL, null=True)
