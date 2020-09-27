from django.db import models
from django.contrib.auth.models import AbstractUser
from pets_schedule import model_choices as mch
from datetime import datetime
from uuid import uuid4


def avatar_pet_path(instace, filename: str):
    ext = filename.split('.')[-1]
    f = str(uuid4())
    filename = f'{f}.{ext}'
    return '/'.join(['avatar', 'pet', str(instace.id), filename])


def avatar_user_path(instace, filename: str):
    ext = filename.split('.')[-1]
    f = str(uuid4())
    filename = f'{f}.{ext}'
    return '/'.join(['avatar', 'user', str(instace.id), filename])


class User(AbstractUser):
    avatar = models.ImageField(upload_to=avatar_user_path, null=True, blank=True, default=None)


class Pet(models.Model):
    name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.PositiveSmallIntegerField(choices=mch.GENDER_CHOICES, default=0)
    kind = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to=avatar_pet_path, null=True, blank=True, default=None)

    @property
    def years_old(self):
        date = datetime.date.today() - self.date_of_birth
        return date.year


class Schedule(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="schedules_pets")
    responsible_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schedules_users")
    name = models.CharField(max_length=50)
    date_time = models.DateTimeField()
