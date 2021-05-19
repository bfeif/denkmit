# imports
import pandas as pd
from flashcards.models import PersonalPronoun,\
    PersonalPronoun_Card

# clear the db
for o in PersonalPronoun.objects.all():
    o.delete()
for o in PersonalPronoun_Card.objects.all():
    o.delete()

# load
de_df = pd.DataFrame.from_dict(
    {
        "Nom": ["ich", "du", "Sie", "er", "sie", "es", "wir", "ihr", "sie"],
        "Dat": ["mir", "dir", "Ihnen", "ihm", "ihr", "ihm", "uns", "euch", "ihnen"],
        "Akk": ["mich", "dich", "Sie", "ihn", "sie", "es", "uns", "euch", "sie"],
        "person_order": [1, 2, 2, 3, 3, 3, 1, 2, 3],
        "plural_order": ["singular", "singular", "formal", "singular", "singular", "singular", "plural", "plural", "plural"]
    }
)

en_df = pd.DataFrame.from_dict(
    {
        "Nom": ["I", "you", "you (formal)", "he", "she", "it", "we", "you (pl)", "they"],
        "Dat": ["me", "you", "you (formal)", "him", "her", "it", "us", "you (pl)", "them"],
        "Akk": ["me", "you", "you (formal)", "him", "her", "it", "us", "you (pl)", "them"],
    }
)

for i in range(len(de_df)):
    for case in ["Nom", "Dat", "Akk"]:
        
        # create and save POS
        p = PersonalPronoun.create(
            word_de=de_df.loc[i][case],
            word_en=en_df.loc[i][case],
            plural_order=de_df.loc[i]["plural_order"],
            person_order=de_df.loc[i]["person_order"],
            case=case
        )
