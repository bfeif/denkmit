from flashcards.models import Noun, NounGenderGuess_Score, \
    NounPluralizationGuess_Score

card_types = [NounGenderGuess_Score, NounPluralizationGuess_Score]

word_de = ["Haus", "Strand", "Lösung"]
word_en = ["house", "beach", "solution"]
word_de_pl = ["Häuser", "Strände", "Lösungen"]
word_en_pl = ["houses", "beaches", "solutions"]
gender = ["N", "M", "F"]

for i in range(len(word_de)):

    # create noun
    n = Noun(
        word_de = word_de[i],
        word_en = word_en[i],
        word_de_pl = word_de_pl[i],
        word_en_pl = word_en_pl[i],
        gender = gender[i]
    )

    # save noun
    n.save()

    # create and save cards
    for card_type in card_types:
        card = card_type(pos=n)
        card.save()
