from flashcards.models import InfinitiveVerb

word_de = ["sich unterhalten", "sich streiten", "sich beschweren", "sich errinern"]
word_en = ["to talk to", "to argue", "to complain", "to remember"]
word_de_perfekt = ["sich unterhalten", "sich gestritten", "sich beschwert", "sich errinert"]

for i in range(len(word_de)):

    # create noun
    InfinitiveVerb.create(
        word_de = word_de[i],
        word_en = word_en[i],
        word_de_perfekt = word_de_perfekt[i]
    )
