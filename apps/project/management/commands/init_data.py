import traceback

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


def creat_first_superuser_and_roles():
    User = get_user_model()
    if User.objects.all().count() == 0:
        User.objects.create_superuser(
            username=settings.DJANGO_SUPERUSER_USERNAME,
            email=settings.DJANGO_SUPERUSER_EMAIL,
            first_name=settings.DJANGO_SUPERUSER_FIRST_NAME,
            last_name=settings.DJANGO_SUPERUSER_LAST_NAME,
            password=settings.DJANGO_SUPERUSER_PASSWORD,
        )


class Command(BaseCommand):
    help = "Create All Tables"

    def handle(self, *args, **kwargs):
        try:
            creat_first_superuser_and_roles()

        except Exception:
            print(traceback.format_exc())
