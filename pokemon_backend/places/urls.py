

from django.urls import path

from places.views import AreaDetails, LocationDetails, RegionDetails, RegionsList


urlpatterns = [
    path('regions/', RegionsList.as_view()),
    path('regions/<int:pk>/', RegionDetails.as_view()),
    path('location/<int:pk>/', LocationDetails.as_view()),
    path('areas/<int:pk>/', AreaDetails.as_view())
]
