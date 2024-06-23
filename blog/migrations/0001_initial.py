# Generated by Django 5.0.6 on 2024-06-23 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите название",
                        max_length=100,
                        verbose_name="Название",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "body",
                    models.TextField(
                        help_text="Введите содержимое", verbose_name="Содержимое"
                    ),
                ),
                (
                    "image_preview",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blog/photo",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(default=True, verbose_name="Публикация"),
                ),
                (
                    "count_view",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество просмотров"
                    ),
                ),
            ],
            options={
                "verbose_name": "Блог",
                "verbose_name_plural": "Блоги",
                "ordering": ("pk",),
            },
        ),
    ]
