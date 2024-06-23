from django.db import models

# Create your models here.


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
    count_view = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ("pk", )