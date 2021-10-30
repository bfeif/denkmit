# imports
from ankipandas import Collection
import pandas as pd
from flashcards.models import InfinitiveVerb

# load collection
collection = Collection("/Users/benfeifke/code/anarki/data/sunken_bliff/collection.anki2")
notes = collection.notes
cards = collection.cards
card_notes = (cards
 .merge(
     notes,
     how='left',
     left_on='nid',
     right_index=True)
 .sort_values(by='nflds')
)


# load nouns to denkmit
verbs_mask = card_notes.cdeck=='German Verbs - Meaning'
verbs = \
(card_notes
 [verbs_mask]
 .drop_duplicates(subset='nid')
)
verbs['word_en'] = verbs.nflds.str[1]
df_temp = pd.DataFrame(verbs.nflds.str[0].str.split(r'\(([^;]*)\)').to_list(), columns=['verb', 'perfekt', 'dummy'], index=verbs.index)
verbs['word_de'] = df_temp['verb'].str.strip()
verbs['word_de_perfekt'] = df_temp['perfekt'].str.strip()

for ind, verb in verbs.iterrows():
    print(verb.word_de)
    InfinitiveVerb.create(
        word_de=verb.word_de,
        word_en=verb.word_en,
        word_de_perfekt=verb.word_de_perfekt
    )
