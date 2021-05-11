from flashcards.models import Noun

word_de = ["Haus", "Strand", "Lösung"]
word_en = ["house", "beach", "solution"]
word_de_pl = ["Häuser", "Strände", "Lösungen"]
word_en_pl = ["houses", "beaches", "solutions"]
gender = ["N", "M", "F"]

for i in range(len(word_de)):
	n = Noun(
		word_de = word_de[i],
		word_en = word_en[i],
		word_de_pl = word_de_pl[i],
        word_en_pl = word_en_pl[i],
		gender = gender[i]
	)
	n.save()