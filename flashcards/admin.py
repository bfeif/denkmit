from django.contrib import admin

from .models import *

mods = [
    
    # POS
    Verb,
    Noun,
    PersonalPronoun,
    Article,

    # Card
    NounGenderGuess_Card,
    NounPluralizationGuess_Card,
    PersonalPronoun_Card,
    Article_Card,
]

for mod in [mods]:
    admin.site.register(mod)
