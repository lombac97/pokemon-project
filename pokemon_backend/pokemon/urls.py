

from django.urls import path

from pokemon.views import AreaDetails, LocationDetails, PokemonInfo, RegionDetails, RegionsList


urlpatterns = [
    path('pokemons/<int:pk>/', PokemonInfo.as_view()),
    path('regions/', RegionsList.as_view()),
    path('regions/<int:pk>/', RegionDetails.as_view()),
    path('location/<int:pk>/', LocationDetails.as_view()),
    path('areas/<int:pk>/', AreaDetails.as_view())
    #  path('login', LoginView.as_view(), name='Login'),
]
