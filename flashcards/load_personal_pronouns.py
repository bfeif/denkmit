import pandas as pd
from flashcards.models import PersonalPronoun,\
    PersonalPronoun_Card


de_df = pd.DataFrame.from_dict(
    {
        "Nom": ["ich", "du", "Sie", "er", "sie", "es", "wir", "ihr", "sie"],
        "Dat": ["mir", "dir", "Ihnen", "ihm", "ihr", "ihm", "uns", "euch", "ihnen"],
        "Akk": ["mich", "dich", "Sie", "ihn", "sie", "es", "uns", "euch", "sie"],
        "person": [1, 2, 2, 3, 3, 3, 1, 2, 3],
        "is_plural": [False, False, False, False, False, False, True, True, True]
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
        p = PersonalPronoun(
            word_de=de_df.loc[i][case],
            word_en=en_df.loc[i][case],
            case=case,
            nom_pronoun_de=de_df.loc[i]["Nom"],
            person=de_df.loc[i]["person"],
            is_plural=de_df.loc[i]["is_plural"]
        )
        p.save()

        # create card(s) accordingly
        p_card = PersonalPronoun_Card(pos=p)
        p_card.save()
