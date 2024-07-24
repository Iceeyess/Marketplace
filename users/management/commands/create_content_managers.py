from django.core.management import BaseCommand
from django.db import IntegrityError

from users.models import User
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        """
        perms_list = ('change_blog', 'delete_blog', )
        perms_list = [Permission.objects.get(codename=_CODENAME) for _CODENAME in perms_list]
        new_group, is_created_group = Group.objects.get_or_create(name='content_manager')
        for perms in perms_list:
            try:
                new_group.permissions.get(codename=perms)
            except BaseException:
                print('Назначаю полномочия...')
                new_group.permissions.add(perms)
                print('Полномочия были добавлены...')
            finally:
                user = User.objects.get(is_staff=True, email='iceeyesss@yandex.ru')
                new_group.user_set.add(user)


