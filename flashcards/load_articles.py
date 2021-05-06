from flashcards.models import Article

article_de = ["die", "der", "den", "die", "", "", "", ""]
article_en = ["the", "___", "the", "the", "", "", "", ""]
definite = [True] * 4 + [False] * 4
case = ["Nom", "Gen", "Dat", "Akk", "Nom", "Gen", "Dat", "Akk"]
gender = ["P"] * 8

for i in range(8):
	a = Article(article_de=article_de[i],
	article_en=article_en[i],
	definite=definite[i],
	case=case[i],
	gender=gender[i])
	a.save()

article_de = ["das", "des", "dem", "das", "ein", "eines", "einem", "ein"]
article_en = ["the", "___", "the", "the", "a",   "_____", "a", "a"]
definite = [True] * 4 + [False] * 4
case = ["Nom", "Gen", "Dat", "Akk", "Nom", "Gen", "Dat", "Akk"]
gender = ["N"] * 8

for i in range(8):
	a = Article(article_de=article_de[i],
	article_en=article_en[i],
	definite=definite[i],
	case=case[i],
	gender=gender[i])
	a.save()

article_de = ["die", "der", "der", "die", "eine", "einer", "einer", "eine"]
article_en = ["the", "___", "the", "the", "a",   "_____", "a", "a"]
definite = [True] * 4 + [False] * 4
case = ["Nom", "Gen", "Dat", "Akk", "Nom", "Gen", "Dat", "Akk"]
gender = ["F"] * 8

for i in range(8):
	a = Article(article_de=article_de[i],
	article_en=article_en[i],
	definite=definite[i],
	case=case[i],
	gender=gender[i])
	a.save()

article_de = ["der", "des", "dem", "den", "ein", "eines", "einem", "einen"]
article_en = ["the", "___", "the", "the", "a",   "_____", "a", "a"]
definite = [True] * 4 + [False] * 4
case = ["Nom", "Gen", "Dat", "Akk", "Nom", "Gen", "Dat", "Akk"]
gender = ["M"] * 8

for i in range(8):
	a = Article(article_de=article_de[i],
	article_en=article_en[i],
	definite=definite[i],
	case=case[i],
	gender=gender[i])
	a.save()