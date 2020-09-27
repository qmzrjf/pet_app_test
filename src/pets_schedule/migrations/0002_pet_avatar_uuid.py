# Generated by Django 2.2.13 on 2020-09-27 16:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pets_schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='avatar_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
