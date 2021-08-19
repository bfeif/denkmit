import os
from django.db import models
from django.db.models import F, Q
from . import pos_models, revlog_models
from . import defaults
import time, datetime
import random

class Card(models.Model):
    is_suspended = models.BooleanField(default=False)
    last_studied_date = models.DateField(auto_now_add=True)
    num_repetitions = models.IntegerField(default=0)
    ease = models.FloatField(default=defaults.EASE_INIT)
    interval = models.FloatField(default=defaults.INTERVAL_INIT)

    class Meta:
        abstract=True

    def __str__(self):
        return (
            f"{self.pos}:\n" \
            f" - last studied at: {self.last_studied_date} \n" \
            f" - num repetitions: {self.num_repetitions} \n" \
            f" - current ease: {self.ease} \n" \
            f" - current interval: {self.interval} \n"
        )

    # function to generate the deck for a day's study
    @classmethod
    def get_flashcard_deck(cls, deck_size):

        # get all cards for review
        review_cards = \
        (cls
         .objects
         .filter(
            # all cards that should be studied today
            last_studied_date__lte=\
            datetime.date.today() -
            F('interval') * datetime.timedelta(days=1),

            # making sure to exclude new cards
            num_repetitions__gt=0)
        )

        # get new cards, if there's space in today's deck, but not more than max
        num_new_card_space = min(deck_size - review_cards.count(), cls.get_num_new_cards_per_day())
        if num_new_card_space > 0:
            new_cards = \
            (cls
            .objects
            .filter(num_repetitions__exact=0)
            .order_by('?')
            [:num_new_card_space])

            # combine for the whole deck
            return list(review_cards) + list(new_cards)

        # else, return just the review cards
        else:
            return list(review_cards)

    # function to get max_new_cards_per_day
    @classmethod
    def get_num_new_cards_per_day(self):
        return defaults.MAX_NEW_CARDS_PER_DAY

    # function to run a flashcard deck for the day of studying
    @classmethod
    def run_flashcard_deck(cls, deck_size=defaults.MAX_CARDS_PER_DAY):

        # get the flashcard deck
        deck = cls.get_flashcard_deck(deck_size)
        print(f'{len(deck)} cards to study today.')

        # run through the deck until each card no longer needs studying today
        deck_finished = False
        card_index = 1
        while len(deck) > 0:
            for card in deck:
                print(f"running flashcard {card_index}")
                card.study_and_update_flashcard()
                print("------------\n")
                card_index+=1
                os.system('clear')
            deck = [card for card in deck if card.interval<1]

    def rate_flashcard_string(self):
        return (
            "Rate difficulty (1-4)\n" \
            "  - 1 (Easy)\n" \
            "  - 2 (Good)\n" \
            "  - 3 (Difficult)\n" \
            "  - 4 (No idea; show it again this session)\n\n" \
            "Difficulty: ")

    def update_card_srs_metrics(self, rating):

        # compute all the new settings
        last_studied_date_new = datetime.date.today()
        num_repetitions_new = self.num_repetitions + 1
        ease_new = defaults.EASE_MODIFIER_DIC[rating] * self.ease
        if rating == 1:
            interval_new = max(1, 3.75 * ease_new * defaults.INTERVAL_MODIFIER * self.interval)
        elif rating == 2:
            interval_new = max(.75, 2.5  * ease_new * defaults.INTERVAL_MODIFIER * self.interval)
        elif rating == 3:
            interval_new = 1.25 * ease_new * defaults.INTERVAL_MODIFIER * self.interval
        elif rating == 4:
            interval_new = .5 # run it again and reset the card
        else:
            print("Invalid rating entered, not updating anything")
            return

        # set all the new settings to the object
        self.last_studied_date = last_studied_date_new
        self.num_repetitions = num_repetitions_new
        self.ease = ease_new
        self.interval = interval_new
        self.save()

    # function to parse input
    def get_and_parse_difficulty_input(self):
        try:
            return int(input())
        except ValueError:
            return None

    # function to study a card, and update its srs stats
    def study_and_update_flashcard(self):

        # show the question
        print(self.flashcard_question_str() + '  (...Hit ENTER to show the answer...)')
        flashcard_start_timestamp = time.time()

        # wait for the user to request showing the answer, then show it
        # input("Hit ENTER to show the answer...")
        # print(self.flashcard_question_str())
        input()
        print(self.flashcard_answer_str())

        # get the user's rating; escape the card if the rating isn't legal
        print(self.rate_flashcard_string())
        rating = self.get_and_parse_difficulty_input()
        while rating not in defaults.POSSIBLE_RATINGS:
            print('Illegal entry. Reenter \nDifficulty:')
            rating = self.get_and_parse_difficulty_input()
        duration = time.time() - flashcard_start_timestamp

        # generate and save the rev_log
        self.revlogs.create(
            duration=duration,
            rating=rating,
            card=self)

        # update the card's memory metrics
        self.update_card_srs_metrics(rating)


class EnDeMeaning_Card(Card):

    class Meta:
        abstract = True

    def flashcard_question_str(self):
        return f"{self.pos.word_en}: _____"

    def flashcard_answer_str(self):
        return f"{self.pos.word_en}: {str(self.pos)}"


class DeEnMeaning_Card(Card):

    class Meta:
        abstract = True

    def flashcard_question_str(self):
        return f"{str(self.pos)}: _____"

    def flashcard_answer_str(self):
        return f"{str(self.pos)}: {self.pos.word_en}"


class NounEnDeMeaning_Card(EnDeMeaning_Card):
    pos = models.OneToOneField(pos_models.Noun, on_delete=models.CASCADE, null=True)


class NounDeEnMeaning_Card(DeEnMeaning_Card):
    pos = models.OneToOneField(pos_models.Noun, on_delete=models.CASCADE, null=True)


class NounGenderGuess_Card(Card):
    pos = models.OneToOneField(pos_models.Noun, on_delete=models.CASCADE, null=True)

    def flashcard_question_str(self):
        return f"___ {self.pos.word_de}"

    def flashcard_answer_str(self):
        article = pos_models.Article.objects.get(gender=self.pos.gender, case="Nom", definite=True).word_de
        return f"{article} {self.pos.word_de} (die {self.pos.word_de_pl})"


class NounPluralizationGuess_Card(Card):
    pos = models.OneToOneField(pos_models.Noun, on_delete=models.CASCADE, null=True)

    def flashcard_question_str(self):
        article = pos_models.Article.objects.get(gender=self.pos.gender, case="Nom", definite=True).word_de
        return f"{article} {self.pos.word_de} (die ______)"

    def flashcard_answer_str(self):
        article = pos_models.Article.objects.get(gender=self.pos.gender, case="Nom", definite=True).word_de
        return f"{article} {self.pos.word_de} (die {self.pos.word_de_pl})"


class PersonalPronoun_Card(Card):
    pos = models.OneToOneField(pos_models.PersonalPronoun, on_delete=models.CASCADE, null=True)

    def flashcard_question_str(self):
        # return f"{self.pos.plural_order}, {self.pos.person_order}, {self.pos.case} (\"{self.pos.word_en}\"): ___"
        if self.pos.case=="Nom":
            return f"{self.pos.word_en}: ____"
        if self.pos.case=="Dat":
            return f"Ich habe ____ ein Geschenk gegeben. ({self.pos.word_en})"
        if self.pos.case=="Akk":
            return f"Ich liebe ____. ({self.pos.word_en})"


    def flashcard_answer_str(self):
        if self.pos.case=="Nom":
            return f"{self.pos.word_en}: {self.pos.word_de}"
        if self.pos.case=="Dat":
            return f"Ich habe {self.pos.word_de} ein Geschenk gegeben. ({self.pos.word_en})"
        if self.pos.case=="Akk":
            return f"Ich liebe {self.pos.word_de}. ({self.pos.word_en})"


class Article_Card(Card):
    pos = models.OneToOneField(pos_models.Article, on_delete=models.CASCADE, null=True)

    def flashcard_question_str(self):
        return f"{self.pos.gender}, {self.pos.case}, {self.pos.definite} (\"{self.pos.word_en}\"): ___"

    def flashcard_answer_str(self):
        return f"{self.pos.gender}, {self.pos.case}, {self.pos.definite} (\"{self.pos.word_en}\"): {self.pos.word_de}"


class PrepositionDeclination_Card(Card):
    pos = models.OneToOneField(pos_models.Preposition, on_delete=models.CASCADE, null=True)

    # overwrite parent class to return not-default. this is bad, and this should be rather stored in config some way smh
    @classmethod
    def get_num_new_cards_per_day(self):
        return 1

    def flashcard_question_str(self):
        # ephemerally set noun and article. take care to get only familiar nouns, as this exercise tests only knowing the case of the preposition.
        familiar_noun = NounDeEnMeaning_Card.objects.filter(ease__gt=1.7).order_by('?').first().pos
        corresponding_article = pos_models.Article.objects.get(gender=familiar_noun.gender, case=self.pos.case, definite=True)
        setattr(self, 'noun', familiar_noun)
        setattr(self, 'article', corresponding_article)

        # return flashcard string
        return f"{self.pos.word_de} ____ {self.noun.word_de} ({self.noun.gender}, ___)"

    def flashcard_answer_str(self):
        # noun and article have already been ephemerally set
        return f"{self.pos.word_de} {self.article.word_de} {self.noun.word_de} ({self.noun.gender}, {self.pos.case})"


class InfinitiveVerbEnDeMeaning_Card(EnDeMeaning_Card):
    pos = models.OneToOneField(pos_models.InfinitiveVerb, on_delete=models.CASCADE, null=True)


class InfinitiveVerbDeEnMeaning_Card(DeEnMeaning_Card):
    pos = models.OneToOneField(pos_models.InfinitiveVerb, on_delete=models.CASCADE, null=True)


