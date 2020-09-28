from django.urls import path
from pets_schedule.api.views import PetsView, PetView, ScheduleView


urlpatterns = [
    path("pets/", PetsView.as_view(), name="pets"),
    path("pets/<int:pk>", PetView.as_view(), name="pet"),
    path("schedule/", ScheduleView.as_view(), name="schedule"),
]
