from django.db import models
from . import pos_models, revlog_models
from . import card_defaults
import time

class Card(models.Model):
    last_studied_utc = models.DateTimeField(auto_now_add=True)
    ease = models.FloatField(default=card_defaults.EASE_INIT)
    interval = models.FloatField(default=card_defaults.INTERVAL_INIT)
    num_repetitions = models.IntegerField(default=0)

    class Meta:
        abstract=True

    # function to generate a flashcard deck for the day of studying
    @classmethod
    def run_flashcard_deck(cls):

        # get the deck of cards for the study session
        card_list = cls.objects.all() # TODO: change to be only the relevant flashcards, i.e. the ones that need to be practiced for the day.
        deck_length=card_list.count()

        # do a flashcard for each noun in the deck
        for index, card in enumerate(card_list[0:2]):
            print(f"running flashcard {index + 1}")
            card.run_flashcard()
            print("------------\n")

    def rate_flashcard_string(self):
        return (
            "Rate difficulty (1-4)\n" \
            "  - 1 (No idea; show it again this session)\n" \
            "  - 2 (Difficult)\n" \
            "  - 3 (Good)\n" \
            "  - 4 (Easy)\n" \
            "Difficulty: ")


    # function to generate and study a flashcard
    def run_flashcard(self):

        # show the question
        print(self.flashcard_question_str())
        flashcard_start_timestamp = time.time()

        # wait for the user to request showing the answer, then show it
        input("Hit ENTER to show the answer...")
        print(self.flashcard_question_str())
        print(self.flashcard_answer_str())

        # get the user's rating
        print(self.rate_flashcard_string())
        rating = input()
        duration = time.time() - flashcard_start_timestamp

        # generate and save the rev_log
        self.revlogs.create(
            duration=duration,
            rating=rating,
            card=self)


class NounGenderGuess_Card(Card):
    pos = models.OneToOneField(pos_models.Noun, on_delete=models.SET_NULL, null=True)

    def flashcard_question_str(self):
        return f"___ {self.pos.word_de}"

    def flashcard_answer_str(self):
        article = pos_models.Article.objects.get(gender=self.pos.gender, case="Nom", definite=True).word_de
        return f"{article} {self.pos.word_de} (die {self.pos.word_de_pl})"


class NounPluralizationGuess_Card(Card):
    pos = models.OneToOneField(pos_models.Noun, on_delete=models.SET_NULL, null=True)

    def flashcard_question_str(self):
        article = pos_models.Article.objects.get(gender=self.pos.gender, case="Nom", definite=True).word_de
        return f"{article} {self.pos.word_de} (die ______)"

    def flashcard_answer_str(self):
        article = pos_models.Article.objects.get(gender=self.pos.gender, case="Nom", definite=True).word_de
        return f"{article} {self.pos.word_de} (die {self.pos.word_de_pl})"


class PersonalPronoun_Card(Card):
    pos = models.OneToOneField(pos_models.PersonalPronoun, on_delete=models.SET_NULL, null=True)

    def flashcard_question_str(self):
        return f"{self.pos.nom_pronoun_de}, {self.pos.case} (\"{self.pos.word_en}\"): ___"

    def flashcard_answer_str(self):
        return f"{self.pos.nom_pronoun_de}, {self.pos.case} (\"{self.pos.word_en}\"): {self.pos.word_de}"
