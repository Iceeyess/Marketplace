from django.db import models
from datetime import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории',
                            help_text='Введите строку названия категории')
    description = models.TextField(verbose_name='Описание категории', help_text='Введите описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара', help_text='Введите строку названия товара')
    description = models.TextField(verbose_name='Описание товара', help_text='Введите описание товара')
    image_preview = models.ImageField(upload_to="products/photo", blank=True, null=True, verbose_name="Фото", help_text="Загрузите фото товара", )
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(verbose_name='Стоимость товара', help_text='Введите строку стоимости товара')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manufactured_at = models.DateTimeField(default=datetime.now, verbose_name='Дата производства товара', help_text='Введите дату производства названия товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)
