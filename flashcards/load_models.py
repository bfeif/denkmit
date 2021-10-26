import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'denkmit.settings'
django.setup()
import pandas as pd
from flashcards.models import Article, Preposition, InfinitiveVerb, Noun, PersonalPronoun

for name, part_of_speech in [('article', Article), ('preposition', Preposition), ('infinitive_verb', InfinitiveVerb), 
                             ('noun', Noun), ('personal_pronoun', PersonalPronoun)]:
    df = pd.read_csv(f"/Users/benfeifke/code/denkmit/data/{name}_table.csv").fillna('')
    records = df.to_dict(orient='records')
    for record in records:
        part_of_speech.create(**record)