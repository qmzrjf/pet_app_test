from django.contrib import admin
from pets_schedule.models import User, Pet, Schedule


class UserAdmin(admin.ModelAdmin):
    fields = ["email", "username", "avatar"]


class PetAdmin(admin.ModelAdmin):
    fields = ["name", "date_of_birth", "gender", "kind", "breed", "avatar"]


class ScheduleAdmin(admin.ModelAdmin):
    fields = ["name", "pet", "responsible_person", "date_time"]


admin.site.register(User, UserAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Schedule, ScheduleAdmin)
