# Generated by Django 5.1.3 on 2024-12-14 03:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0004_alter_fooditem_category_alter_fooditem_price"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ordermodel",
            old_name="created_on",
            new_name="order_date",
        ),
        migrations.RemoveField(
            model_name="menuitem",
            name="description",
        ),
        migrations.RemoveField(
            model_name="menuitem",
            name="img",
        ),
        migrations.RemoveField(
            model_name="ordermodel",
            name="price",
        ),
        migrations.AddField(
            model_name="ordermodel",
            name="customer_name",
            field=models.CharField(default="Unknown", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ordermodel",
            name="total_price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.RemoveField(
            model_name="fooditem",
            name="category",
        ),
        migrations.RemoveField(
            model_name="menuitem",
            name="category",
        ),
        migrations.AlterField(
            model_name="ordermodel",
            name="items",
            field=models.ManyToManyField(to="customer.menuitem"),
        ),
        migrations.CreateModel(
            name="Order",
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
                ("quantity", models.IntegerField()),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "food_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.fooditem",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="fooditem",
            name="category",
            field=models.ManyToManyField(
                related_name="food_items", to="customer.category"
            ),
        ),
        migrations.AddField(
            model_name="menuitem",
            name="category",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
