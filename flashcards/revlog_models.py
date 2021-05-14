from django.db import models
from .pos_models import *
import time

# RevLog models
class RevLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True) # the datetime that the review gets added
    duration = models.IntegerField() # the time spent on the flashcard
    rating = models.IntegerField() # the review difficulty logged (1, 2, 3, 4) TODO change to Integer choice

    class Meta:
        abstract=True

    def __str__(self):
        return f"""{self.pos}:\n - study_timestamp: {self.timestamp}\n - study_duration: {self.duration}\n - study_rating: {self.rating}"""

    # function to generate a flashcard deck for the day of studying
    @classmethod
    def run_flashcard_deck(cls):

        # get the deck of nouns for the study session
        pos_list = (
            cls
            ._meta
            .get_field('pos')
            .related_model
            .objects
            .all()) # TODO: change to be only the relevant flashcards, i.e. the ones that need to be practiced for the day.
        deck_length=pos_list.count()

        # do a flashcard for each noun in the deck
        for index, pos in enumerate(pos_list[0:2]):
            print(f"running flashcard {index + 1}")
            cls.run_flashcard(pos)
            print("------------\n")

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
    def run_flashcard(cls, pos):
        
        # generate the flashcard
        rev_log = cls(duration=5, rating=2, pos=pos)
        
        # show the question
        print(rev_log.flashcard_question_str())
        flashcard_start_timestamp = time.time()

        # wait for the user to request showing the answer, then show it
        input("Hit ENTER to show the answer...")
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
    pos = models.ForeignKey('Noun', on_delete=models.SET_NULL, null=True) # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)

    def flashcard_question_str(self):
        return f"___ {self.pos.word_de}"

    def flashcard_answer_str(self):
        article = Article.objects.get(gender=self.pos.gender, case="Nom", definite=True).word_de
        return f"{article} {self.pos.word_de} (die {self.pos.word_de_pl})"


class NounPluralizationGuess_RevLog(RevLog):
    pos = models.ForeignKey('Noun', on_delete=models.SET_NULL, null=True) # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)

    def flashcard_question_str(self):
        article = Article.objects.get(gender=self.pos.gender, case="Nom", definite=True).word_de
        return f"{article} {self.pos.word_de} (die ______)"

    def flashcard_answer_str(self):
        article = Article.objects.get(gender=self.pos.gender, case="Nom", definite=True).word_de
        return f"{article} {self.pos.word_de} (die {self.pos.word_de_pl})"

class PersonalPronoun_RevLog(RevLog):
    pos = models.ForeignKey('PersonalPronoun', on_delete=models.SET_NULL, null=True) # TODO change to make on_delete plug in the foreign key's word (i.e. instead of id)

    def flashcard_question_str(self):
        return f"{self.pos.nom_pronoun_de}, {self.pos.case} (\"{self.pos.word_en}\"): ___"

    def flashcard_answer_str(self):
        return f"{self.pos.nom_pronoun_de}, {self.pos.case} (\"{self.pos.word_en}\"): {self.pos.word_de}"