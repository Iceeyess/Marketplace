from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            username='Admin',
            email='ice_eyes@mail.ru',
            is_superuser=True,
            is_staff=True,
            is_active=True,
            first_name='Дмитрий',
            last_name='Крашенинников',
        )
        user.set_password('123456')
        user.save()
