from django.db import models
from . import pos_models, revlog_models
from .. import defaults
import time, datetime

class Card(models.Model):
    is_suspended = models.BooleanField(default=False)
    last_studied_utc = models.DateTimeField(auto_now_add=True)
    num_repetitions = models.IntegerField(default=0)
    ease = models.FloatField(default=defaults.EASE_INIT)
    interval = models.FloatField(default=defaults.INTERVAL_INIT)

    class Meta:
        abstract=True

    def __str__(self):
        return (
            f"{self.pos}:\n" \
            f" - last studied at: {self.last_studied_utc} \n" \
            f" - num repetitions: {self.num_repetitions} \n" \
            f" - current ease: {self.ease} \n" \
            f" - current interval: {self.interval} \n"
        )

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
            "  - 1 (Easy)\n" \
            "  - 2 (Good)\n" \
            "  - 3 (Difficult)\n" \
            "  - 4 (No idea; show it again this session)\n" \
            "Difficulty: ")

    def update_card_srs_metrics(self, rating):

        # compute all the new settings
        last_studied_utc_new = datetime.datetime.now()
        num_repetitions_new = self.num_repetitions + 1
        ease_new = defaults.EASE_MODIFIER_DIC[rating] * self.ease
        if rating == 1:
            interval_new = 3.75 * ease_new * defaults.INTERVAL_MODIFIER * self.interval
        elif rating == 2:
            interval_new = 2.5  * ease_new * defaults.INTERVAL_MODIFIER * self.interval
        elif rating == 3:
            interval_new = 1.25 * ease_new * defaults.INTERVAL_MODIFIER * self.interval
        elif rating == 4:
            interval_new = .5 # run it again and reset the card
        else:
            print("Invalid rating entered, not updating anything")
            return

        # set all the new settings to the object
        self.last_studied_utc = last_studied_utc_new
        self.num_repetitions = num_repetitions_new
        self.ease = ease_new
        self.interval = interval_new
        self.save()


    # function to generate and study a flashcard
    def run_flashcard(self):

        # show the question
        print(self.flashcard_question_str())
        flashcard_start_timestamp = time.time()

        # wait for the user to request showing the answer, then show it
        input("Hit ENTER to show the answer...")
        print(self.flashcard_question_str())
        print(self.flashcard_answer_str())

        # get the user's rating; escape the card if the rating isn't legal
        print(self.rate_flashcard_string())
        rating = int(input())
        duration = time.time() - flashcard_start_timestamp
        if rating not in defaults.POSSIBLE_RATINGS:
            print("Invalid rating entered, not updating anything")
            return rating

        # generate and save the rev_log
        self.revlogs.create(
            duration=duration,
            rating=rating,
            card=self)

        # update the card's memory metrics
        self.update_card_srs_metrics(rating)


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
