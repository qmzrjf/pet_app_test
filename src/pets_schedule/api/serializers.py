from pets_schedule.models import Pet, Schedule
from rest_framework import serializers


class PetSerializer(serializers.ModelSerializer):
    schedules = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = (
            "id",
            "name",
            "date_of_birth",
            "years_old",
            "get_gender_display",
            "kind",
            "breed",
            "avatar",
            "schedules",
        )

    def get_schedules(self, obj):
        return self.context["schedules"][:4]


class PetsSerializer(serializers.ModelSerializer):
    schedules_pets__date_time__max = serializers.CharField()

    class Meta:
        model = Pet
        fields = (
            "id",
            "name",
            "years_old",
            "get_gender_display",
            "kind",
            "breed",
            "avatar",
            "schedules_pets__date_time__max",
        )


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = (
            "name",
            "pet",
            "responsible_person",
            "date_time",
        )