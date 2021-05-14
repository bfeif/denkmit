from django.db import models
from . import card_defaults

class CardScore(models.Model):
    last_studied_utc = models.DateTimeField(auto_now_add=True)
    ease = models.FloatField(default=card_defaults.EASE_INIT)
    interval = models.FloatField(default=card_defaults.INTERVAL_INIT)

    class Meta:
        abstract=True
        