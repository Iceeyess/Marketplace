# Generated by Django 5.0.6 on 2024-06-08 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_rename_category_id_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="category",
                to="catalog.category",
            ),
        ),
    ]
