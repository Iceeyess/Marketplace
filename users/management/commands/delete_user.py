from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.get(email='ice_eyes@mail.ru')
        user.delete()
