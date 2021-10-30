from flashcards.models import Verb

verb_de = ["spiele", "laufe", "gebe"]
verb_en = ["play", "walk", "give"]
infinitive_de = ["spielen", "laufen", "geben"]
mood = ["indicative", "indicative", "indicative"]
tense = ["present", "present", "present"]
subject = ["ich", "ich", "ich"]
valency = [2, 1, 3]


for i in range(len(verb_de)):
	v = Verb(
		verb_de = verb_de[i],
		verb_en = verb_en[i],
		infinitive_de = infinitive_de[i],
		mood = mood[i],
		tense = tense[i],
		subject = subject[i],
		valency = valency[i]
	)
	v.save()