# Модуль для функций
from django.conf import settings
from django.core.cache import cache
from django.db.models import QuerySet

from catalog.models import Category


def list_categories() -> QuerySet:
    """Возвращает все категории существующие на данный момент в БД."""
    if settings.CACHE_ENABLED and cache.get('cached_categories'):
        return cache.get('cached_categories')
    else:
        return cache.set('cached_categories', Category.objects.all(), 10)

