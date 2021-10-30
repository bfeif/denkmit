from flashcards.models import Preposition

prepositions = [
    ('bis', 'until', 'Akk'),
    ('durch', 'through', 'Akk'),
    ('für', 'for', 'Akk'),
    ('gegen', 'against', 'Akk'),
    ('ohne', 'without', 'Akk'),
    ('um', 'around', 'Akk'),
    ('ab', 'from', 'Dat'),
    ('aus', 'from', 'Dat'),
    ('außer', 'except for', 'Dat'),
    ('bei', 'by', 'Dat'),
    ('laut', 'according to', 'Dat'),
    ('mit', 'with', 'Dat'),
    ('nach', 'after, to', 'Dat'),
    ('nahe', 'near', 'Dat'),
    ('seit', 'since', 'Dat'),
    ('von', 'from', 'Dat'),
    ('zu', 'to', 'Dat')
]

for preposition in prepositions:
	Preposition.create(
		word_de=preposition[0],
        word_en=preposition[1],
        case=preposition[2]
	)