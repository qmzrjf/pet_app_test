from django.db.models.signals import pre_save
from django.dispatch import receiver

from pets_schedule.models import User, Pet
import os

import shutil
from django.conf import settings


@receiver(pre_save, sender=User)
def pre_save_user_avatar(sender, instance, **kwargs):
    try:
        if instance.avatar is not None:
            shutil.rmtree(
                os.path.join(settings.MEDIA_ROOT, "avatar", "user", str(instance.id))
            )

    except:
        pass


@receiver(pre_save, sender=Pet)
def pre_save_pet_avatar(sender, instance, **kwargs):
    try:
        if instance.avatar is not None:
            shutil.rmtree(
                os.path.join(
                    settings.MEDIA_ROOT, "avatar", "pet", str(instance.avatar_uuid)
                )
            )
    except:
        pass
