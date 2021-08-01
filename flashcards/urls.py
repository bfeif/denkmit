from django.urls import path

from . import views
# from flashcards.views import PrepositionDeclinationCardDeckView

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='index'),
    path('preposition-declination', 
         views.PrepositionDeclinationCardDeckView.as_view(),
         name='preposition-declination')
]