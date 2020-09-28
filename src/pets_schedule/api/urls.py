from django.urls import path
from pets_schedule.api.views import PetsView, PetView, ScheduleView, SchedulesView


urlpatterns = [
    path("pets/", PetsView.as_view(), name="pets"),
    path("pets/<int:pk>", PetView.as_view(), name="pet"),
    path("schedule/", ScheduleView.as_view(), name="schedule"),
    path("schedules/", SchedulesView.as_view(), name="schedules"),
]
{
        "name": "Go to the vet",
        "pet": 8,
        "responsible_person": 4,
        "date_time": "2020-09-28T06:00:00Z"
    }