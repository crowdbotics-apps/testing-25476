# Generated by Django 2.2.19 on 2021-04-05 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Run",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("planned_date", models.DateField(auto_now_add=True)),
                ("closed_datetime", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="List",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=256)),
                ("description", models.TextField()),
                (
                    "items",
                    models.ManyToManyField(
                        related_name="list_items", to="groceries.Item"
                    ),
                ),
            ],
        ),
    ]
