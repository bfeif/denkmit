# set up django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','denkmit.settings')
import django
django.setup()

# imports
from ankipandas import Collection
from flashcards.models import Noun

# env
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
nouns_mask = card_notes.cdeck.str.lower().str.contains('noun')
nouns = \
(card_notes
 [nouns_mask]
 .drop_duplicates(subset='nid')
)
nouns['word_en'] = nouns.nflds.str[1]
nouns['word_de'] = nouns.nflds.str[0].str.split(r'\(([^;]*)\)').str[0].str.split().str[1]
nouns['word_de_pl'] = nouns.nflds.str[0].str.extract(r'\(die ([^;]*)\)')
nouns['word_de_pl'][nouns['word_de_pl'].isnull()] = nouns[nouns['word_de_pl'].isnull()]['word_de'] + '*'
nouns['gender'] = nouns.nflds.str[0].str.split().str[0].map({'der': 'M', 'die': 'F', 'das': 'N'})

for o in Noun.objects.all():
    o.delete()
for ind, noun in nouns.iterrows():
    print(noun.word_de)
    Noun.create(
        word_de=noun.word_de,
        word_en=noun.word_en,
        word_de_pl=noun.word_de_pl,
        gender=noun.gender
    )
