

from django.urls import path

from pokemon.views import OwnPokemonInfo, PokemonInfo


urlpatterns = [
    path('<int:pk>/', PokemonInfo.as_view()),
    path('own', OwnPokemonInfo.as_view()),

]
