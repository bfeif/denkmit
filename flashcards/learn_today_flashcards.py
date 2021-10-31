import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'denkmit.settings'
django.setup()
from config import flashcard_config


exercises_for_today = [model for model, to_study in flashcard_config.FLASHCARD_CONFIG.items() if to_study==True]
for exercise in exercises_for_today:
    exercise.learn_today_flashcard_deck()