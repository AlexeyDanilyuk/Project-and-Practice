# Generated by Django 2.2.3 on 2019-07-09 09:55

from django.conf import settings
from django.db import migrations
from authapp.models import User, UserProfile


def forwards_func(apps, schema_editor):
    if settings.DEBUG:
        try:
            User.objects.create_superuser(
                'django', 'django@geekshop.local', 'geekbrains', first_name='Алексей', last_name='Данилюк', age=42
            )
            to_update = User.objects.filter(userprofile__isnull=True)
            print(len(to_update))
            for user in to_update:
                UserProfile.objects.create(user=user)
        except:
            print("Не получается создать суперпуперпользователя!")


def reverse_func(apps, schema_editor):
    if settings.DEBUG:
        try:
            User.objects.create_superuser(
                'django', 'django@geekshop.local', 'geekbrains', first_name='Алексей', last_name='Данилюк', age=42
            )
            to_update = User.objects.filter(userprofile__isnull=True)
            print(len(to_update))
            for user in to_update:
                UserProfile.objects.create(user=user)
        except:
            print("Не получается удалить суперпуперпользователя!")


class Migration(migrations.Migration):
    dependencies = [("authapp", "0001_initial")]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
