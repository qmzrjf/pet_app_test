from django.contrib import admin
from pets_schedule.models import User, Pet, Schedule


class UserAdmin(admin.ModelAdmin):
    search_fields = ("username",)
    fields = ["email", "username", "avatar"]
    list_display = ("username", "email")
    list_filter = ("username",)
    ordering = ("-date_joined",)


class PetAdmin(admin.ModelAdmin):
    search_fields = ("name", "kind", "breed")
    fields = ["name", "date_of_birth", "gender", "kind", "breed", "avatar"]
    list_display = ("name", "gender", "kind", "breed", "date_of_birth")
    list_filter = ("name", "gender", "kind", "breed")
    ordering = ("-date_of_birth",)


class ScheduleAdmin(admin.ModelAdmin):
    search_fields = ("responsible_person", "pet")
    fields = ["name", "pet", "responsible_person", "date_time"]
    list_display = ("pet", "responsible_person", "name", "date_time")
    list_filter = ("pet", "responsible_person")


admin.site.register(User, UserAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Schedule, ScheduleAdmin)
