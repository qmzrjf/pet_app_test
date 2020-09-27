from django.contrib import admin
from pets_schedule.models import User


class UserAdmin(admin.ModelAdmin):
    fields = ['email', 'username', 'avatar']


admin.site.register(User, UserAdmin)