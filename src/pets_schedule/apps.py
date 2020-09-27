from django.apps import AppConfig


class PetsScheduleConfig(AppConfig):
    name = "pets_schedule"

    def ready(self):
        import pets_schedule.signals
