from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.template import loader
from flashcards.models import *


def index(request):
    template = loader.get_template('flashcards/index.html')
    return HttpResponse(template.render())

def dashboard(request):
    return HttpResponse("You're at the dashboard")

class PrepositionDeclinationCardDeckView(generic.ListView):
    template_name = 'flashcards/preposition_declination_card_deck.html'
    model = PrepositionDeclination_Card
    context_object_name = 'cards'

    def get_context_data(self):
        context = super().get_context_data()
        print(context)
        return context
