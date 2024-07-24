from django.core.management import BaseCommand
from django.db import IntegrityError

from users.models import User
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):

    def handle(self, *args, **options):
        """create moderators group and assign permissions
        if there was group 'moderators' when it will not be created,
        if there were previously created permissions, then it will be created,
        if there is nor permissions, not group 'moderators', then it will
        """
        new_perms = (('delete_public_product', 'Can disable product'),
                     ('change_product_description', 'Can change product description'),
                     ('change_product_category', 'Can change product category'))
        content_type = ContentType.objects.get_for_model(User)
        new_group, is_created_group = Group.objects.get_or_create(name='moderators')

        for codename, name in new_perms:
            perms = Permission.objects.filter(codename=codename)
            if len(perms):
                permission = Permission.objects.create(codename=codename, name=name, content_type=content_type)
                new_group.permissions.add(permission)
                continue
            else:
                permission = Permission.objects.create(codename=codename, name=name, content_type=content_type)
                new_group.permissions.add(permission)
        user = User.objects.get(email='pavlikkrolikov@yandex.ru')
        new_group.user_set.add(user)

