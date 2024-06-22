from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название категории", help_text="Введите строку названия категории"
    )
    description = models.TextField(verbose_name="Описание категории", help_text="Введите описание категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("id",)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара", help_text="Введите строку названия товара")
    description = models.TextField(verbose_name="Описание товара", help_text="Введите описание товара")
    image_preview = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото товара",
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    price = models.FloatField(verbose_name="Стоимость товара", help_text="Введите строку стоимости товара")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("name",)


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя', help_text='Введите имя')
    phone = models.CharField(max_length=10, verbose_name='Телефон', help_text='Введите телефон(не более 10 символов)')
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.phone}"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ("name",)


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', help_text='Введите название')
    slug = models.CharField(max_length=150, null=True, blank=True, unique=True, verbose_name='Slug')
    body = models.TextField(verbose_name='Содержимое', help_text='Введите содержимое')
    image_preview = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_public = models.BooleanField(default=True, verbose_name='Публикация')
    count_view = models.IntegerField(default=0, verbose_name='Количество просмотров')

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ("pk",)