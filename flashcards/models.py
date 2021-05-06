from django.db import models
import time


# POS models
class Noun(models.Model):
    noun_de = models.CharField(max_length=20)
    noun_en = models.CharField(max_length=20)
    noun_de_pl = models.CharField(max_length=20)
    noun_en_pl = models.CharField(max_length=20, default="temporary")
    pluralization_model = models.CharField(max_length=20) # TODO change to Integer choice
    gender = models.CharField(max_length=1) # # TODO change to Integer choice: M, F, N

    def __str__(self):
        gender_dic = {"M": "der", "F": "die", "N": "das", "P": "die"}
        return f"{gender_dic[self.gender]} {self.noun_de} (die {self.noun_de_pl})"


class PersonalPronoun(models.Model):
    pronoun_de = models.CharField(max_length=20)
    pronoun_en = models.CharField(max_length=20)
    case = models.CharField(max_length=3) # TODO change to Integer choice: Nom, Akk, Dat, Gen
    nom_pronoun_de = models.CharField(max_length=10, default="temporary") # TODO change to Integer choice (ich, du, er, sie, es, wir, ihr, Sie)
    person = models.IntegerField() # 1st person, 2nd person, 3rd person
    is_plural = models.BooleanField(default=False)

    def __str__(self):
        return f"({self.nom_pronoun_de}, {self.case}): {self.pronoun_de}"
    
    class Meta:
        unique_together = ("nom_pronoun_de", "case", "person", "is_plural")


class Article(models.Model):
    article_de = models.CharField(max_length=10) # the article in german
    article_en = models.CharField(max_length=10) # the article in german english
    case = models.CharField(max_length=3) # TODO change to Integer choice: Nom, Akk, Dat, Gen
    gender = models.CharField(max_length=1) # TODO change to Integer choice: M, F, N
    definite = models.BooleanField() # definite or indefinite

    def __str__(self):
        return f"({self.gender}, {self.case}, {self.definite}): {self.article_de}"

    class Meta:
        unique_together = ("case", "gender", "definite")


class Verb(models.Model):
    verb_de = models.CharField(max_length=20)
    verb_en = models.CharField(max_length=20)
    infinitive_de = models.CharField(max_length=20, default="temporary")
    mood = models.CharField(max_length=10) # TODO change to Integer choice
    tense = models.CharField(max_length=10) # TODO change to Integer choice
    subject = models.CharField(max_length=10) # TODO change to Integer choice (ich, du, er_sie_es, wir, ihr, Sie)
    valency = models.IntegerField() # TODO change to Integer choice as per https://en.wikipedia.org/wiki/Verb#Valency
    # TODO: phrasal verbs and the requisite fields

    def __str__(self):
        return f"({self.infinitive_de}, {self.mood}, {self.tense}, {self.subject}): {self.verb_de}"

    class Meta:
        unique_together = ("infinitive_de", "mood", "tense", "subject") # every verb conjugation has an infinitive, a grammatical mood, a temporal-tense, and a subject that's conjugating it.


# RevLog models
class RevLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True) # the datetime that the review gets added
    duration = models.IntegerField() # the time spent on the flashcard
    rating = models.IntegerField() # the review difficulty logged (1, 2, 3, 4) TODO change to Integer choice

    class Meta:
        abstract=True

    def __str__(self):
        return f"""\n- study_timestamp: {self.timestamp}\n- study_duration: {self.duration}\n- study_rating: {self.rating}"""

    @classmethod
    def rate_flashcard_string(self):
        return (
            "Rate difficulty (1-4)\n" \
            "  - 1 (No idea; show it again this session)\n" \
            "  - 2 (Difficult)\n" \
            "  - 3 (Good)\n" \
            "  - 4 (Easy)\n" \
            "Difficulty: ")

    # function to generate and study a flashcard
    @classmethod
    def run_flashcard(cls, noun):
        
        # generate the flashcard
        rev_log = cls(duration=5, rating=2, noun=noun)
        
        # show the question
        print(rev_log.flashcard_question_str())
        flashcard_start_timestamp = time.time()

        # wait for the user to request showing the answer, then show it
        input("Press any key to show the answer...")
        print(rev_log.flashcard_question_str())
        print(rev_log.flashcard_answer_str())

        # get the user's rating
        print(cls.rate_flashcard_string())
        rating = input()
        duration = time.time() - flashcard_start_timestamp

        # save the rev_log
        rev_log.duration = duration
        rev_log.rating = rating
        rev_log.save()


class NounGenderGuess_RevLog(RevLog):
    noun = models.ForeignKey('Noun', on_delete=models.SET_NULL, null=True) # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)

    def __str__(self):
        return f"""{self.noun}:{super().__str__()}"""

    def flashcard_question_str(self):
        return f"___ {self.noun.noun_de}"

    def flashcard_answer_str(self):
        article = Article.objects.get(gender=self.noun.gender, case="Nom", definite=True).article_de
        return f"{article} {self.noun.noun_de} (die {self.noun.noun_de_pl})"

    # function to generate a flashcard deck for the day of studying
    @classmethod
    def run_flashcard_deck(cls):

        # get the deck of nouns for the study session
        nouns = Noun.objects.all() # TODO: change to be only the relevant flashcards, i.e. the ones that need to be practiced for the day.
        deck_length=nouns.count()

        # do a flashcard for each noun in the deck
        for index, noun in enumerate(nouns):
            print(f"running flashcard {index}")
            cls.run_flashcard(noun)
            print("------------\n")

class NounPluralizationGuess_RevLog(RevLog):
    noun = models.ForeignKey('Noun', on_delete=models.SET_NULL, null=True) # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)
    
    def __str__(self):
        return f"""{self.noun}:{super().__str__()}"""

    def flashcard_question_str(self):
        article = Article.objects.get(gender=self.noun.gender, case="Nom", definite=True).article_de
        return f"{article} {self.noun.noun_de} (die ______)"

    def flashcard_answer_str(self):
        article = Article.objects.get(gender=self.noun.gender, case="Nom", definite=True).article_de
        return f"{article} {self.noun.noun_de} (die {self.noun.noun_de_pl})"

    # function to generate a flashcard deck for the day of studying
    @classmethod
    def run_flashcard_deck(cls):

        # get the deck of nouns for the study session
        nouns = Noun.objects.all() # TODO: change to be only the relevant flashcards, i.e. the ones that need to be practiced for the day.
        deck_length=nouns.count()

        # do a flashcard for each noun in the deck
        for index, noun in enumerate(nouns):
            print(f"running flashcard {index}")
            cls.run_flashcard(noun)
            print("------------\n")

class PersonalPronoun_RevLog(RevLog):
    '''
    Generates flashcards of the form:
    {"We eat chocolate": "__ essen Schokolade"}
    {"He loves me": "Er liebt ___"}
    {"I give you food": "Ich gebe ___ Essen"}

    This model 
    '''
    personal_pronoun = models.ForeignKey('Noun', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"""{self.personal_pronoun}:{super().__str__()}"""
    
    def generate_flashard_question_and_answer_str(self):
        '''
        '''
        pass

    def flashcard_question_str(self):
        pass

    def flashcard_answer_str(self):
        pass

    # function to generate a flashcard deck for the day of studying
    @classmethod
    def run_flashcard_deck(cls):

        # get the deck of nouns for the study session
        personal_pronouns = PersonalPronoun.objects.all() # TODO: change to be only the relevant flashcards, i.e. the ones that need to be practiced for the day.
        deck_length=nouns.count()

        # do a flashcard for each noun in the deck
        for index, noun in enumerate(nouns):
            print(f"running flashcard {index}")
            cls.run_flashcard(noun)
            print("------------\n")
