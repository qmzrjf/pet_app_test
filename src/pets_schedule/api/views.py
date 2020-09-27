from django.http import HttpResponse, JsonResponse
import json
from rest_framework import generics

from pets_schedule.models import Pet
from pets_schedule.api.serializers import PetSerializer


class PetsView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
