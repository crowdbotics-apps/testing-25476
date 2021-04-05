from django.conf import settings
from django.db import models


class Item(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    description = models.TextField()


class List(models.Model):
    "Generated Model"
    label = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    items = models.ManyToManyField(
        "groceries.Item",
        related_name="list_items",
    )


class Run(models.Model):
    "Generated Model"
    planned_date = models.DateField(
        auto_now_add=True,
    )
    closed_datetime = models.DateTimeField()
    list = models.ForeignKey(
        "groceries.List",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="run_list",
    )


# Create your models here.
