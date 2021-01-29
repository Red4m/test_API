# Generated by Django 3.1.5 on 2021-01-26 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Laptops",
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
                ("device", models.IntegerField(default=0, verbose_name="device")),
                (
                    "configuration",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=255,
                        verbose_name="configuration",
                    ),
                ),
                (
                    "price",
                    models.FloatField(
                        blank=True,
                        default=0,
                        help_text="указывать сумму в долларах",
                        verbose_name="price",
                    ),
                ),
                (
                    "paid_by",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="paid_by"
                    ),
                ),
                (
                    "team",
                    models.CharField(
                        blank=True, default=None, max_length=255, verbose_name="team"
                    ),
                ),
                ("comment", models.TextField(blank=True, default=None)),
                (
                    "item_number",
                    models.PositiveSmallIntegerField(
                        blank=True, verbose_name="item_number"
                    ),
                ),
                ("date", models.DateField(blank=True, verbose_name="date")),
            ],
        ),
    ]
