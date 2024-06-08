from django.core.management import BaseCommand
from catalog.models import Category, Product
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        # Здесь мы получаем данные из фикстурв с категориями
        with open('catalog.json') as f:
            return json.load(f)

    def handle(self, *args, **options):

        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for d_dict in Command.json_read_categories():
            if d_dict['model'] == 'catalog.category':
                category_for_create.append(
                    Category(
                        pk=d_dict['pk'], name=d_dict['fields']['name'], description=d_dict['fields']['description']
                            )
                )
            elif d_dict['model'] == 'catalog.product':
                product_for_create.append(
                    Product(pk=d_dict['pk'], name=d_dict['fields']['name'], description=d_dict['fields']['description'],
                            price=d_dict['fields']['price'], image_preview=d_dict['fields']['image_preview'],
                            category=Category.objects.get(pk=d_dict['fields']['category']),
                            created_at=d_dict['fields']['created_at'], updated_at=d_dict['fields']['updated_at']
                            )
                )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)
