from flashcards.models import Article

word_de = ["die", "der", "den", "die", "", "", "", ""]
word_en = ["the", "___", "the", "the", "", "", "", ""]
definite = [True] * 4 + [False] * 4
case = ["Nom", "Gen", "Dat", "Akk", "Nom", "Gen", "Dat", "Akk"]
gender = ["P"] * 8

for i in range(8):
    a = Article(word_de=word_de[i],
    word_en=word_en[i],
    definite=definite[i],
    case=case[i],
    gender=gender[i])
    if a.case=="Gen":
        a.is_suspended=True
    a.save()

word_de = ["das", "des", "dem", "das", "ein", "eines", "einem", "ein"]
word_en = ["the", "___", "the", "the", "a",   "_____", "a", "a"]
definite = [True] * 4 + [False] * 4
case = ["Nom", "Gen", "Dat", "Akk", "Nom", "Gen", "Dat", "Akk"]
gender = ["N"] * 8

for i in range(8):
    a = Article(word_de=word_de[i],
    word_en=word_en[i],
    definite=definite[i],
    case=case[i],
    gender=gender[i])
    if a.case=="Gen":
        a.is_suspended=True
    a.save()

word_de = ["die", "der", "der", "die", "eine", "einer", "einer", "eine"]
word_en = ["the", "___", "the", "the", "a",   "_____", "a", "a"]
definite = [True] * 4 + [False] * 4
case = ["Nom", "Gen", "Dat", "Akk", "Nom", "Gen", "Dat", "Akk"]
gender = ["F"] * 8

for i in range(8):
    a = Article(word_de=word_de[i],
    word_en=word_en[i],
    definite=definite[i],
    case=case[i],
    gender=gender[i])
    if a.case=="Gen":
        a.is_suspended=True
    a.save()

word_de = ["der", "des", "dem", "den", "ein", "eines", "einem", "einen"]
word_en = ["the", "___", "the", "the", "a",   "_____", "a", "a"]
definite = [True] * 4 + [False] * 4
case = ["Nom", "Gen", "Dat", "Akk", "Nom", "Gen", "Dat", "Akk"]
gender = ["M"] * 8

for i in range(8):
    a = Article(word_de=word_de[i],
    word_en=word_en[i],
    definite=definite[i],
    case=case[i],
    gender=gender[i])
    if a.case=="Gen":
        a.is_suspended=True
    a.save()