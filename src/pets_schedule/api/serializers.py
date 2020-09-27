from pets_schedule.models import Pet
from rest_framework import serializers


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = (
            'id',
            'name',
            'date_of_birth',
            'years_old',
            'get_gender_display',
            'kind',
            'breed',
            'avatar',
        )
