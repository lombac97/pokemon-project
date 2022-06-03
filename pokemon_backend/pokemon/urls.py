

from django.urls import path

from pokemon.views import OwnPokemonInfo, OwnPokemonPartyInfo, PokemonInfo, SwapPokemonStorage


urlpatterns = [
    path('<int:pk>/', PokemonInfo.as_view()),
    path('own/', OwnPokemonInfo.as_view()),
    path('own/<int:pk>/', OwnPokemonInfo.as_view()),
    path('own/party/', OwnPokemonPartyInfo.as_view()),
    path('own/swap/', SwapPokemonStorage.as_view())
]
