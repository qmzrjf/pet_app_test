from rest_framework import generics
from django.db.models import Max

from pets_schedule.models import Pet, Schedule
from pets_schedule.api.serializers import PetSerializer, PetsSerializer, ScheduleSerializer


class PetsView(generics.ListAPIView):
    queryset = Pet.objects.annotate(Max("schedules_pets__date_time"))
    serializer_class = PetsSerializer


class PetView(generics.RetrieveUpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get_serializer_context(self):
        context = super(PetView, self).get_serializer_context()
        schedules = (
            Schedule.objects.all()
            .filter(pet=self.kwargs["pk"])
            .values("name", "date_time", "responsible_person", "status")
            .order_by("-date_time")
        )
        context.update({"schedules": schedules})
        return context


class ScheduleView(generics.CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
