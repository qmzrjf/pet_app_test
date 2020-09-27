from django.urls import path
from pets_schedule.api.views import PetsView, PetView


urlpatterns = [
    path('pets/', PetsView.as_view(), name='pets'),
    path('pets/<int:pk>', PetView.as_view(), name='pet'),


]