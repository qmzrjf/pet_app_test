# Generated by Django 2.2.13 on 2020-09-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_schedule', '0002_pet_avatar_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]