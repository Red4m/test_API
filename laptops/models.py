from django.db import models

from employee.models import Employee


class Laptops(models.Model):
    device = models.IntegerField(verbose_name="device", default=0)
    configuration = models.ImageField(
        verbose_name="configuration", upload_to="images/", null=True, blank=True
    )
    price = models.FloatField(
        verbose_name="price",
        default=0,
        help_text="указывать сумму в долларах",
        blank=True,
    )
    paid_by = models.CharField(verbose_name="paid_by", max_length=255, blank=True)
    team = models.CharField(
        verbose_name="team", max_length=255, default=None, blank=True
    )
    comment = models.TextField(default=None, blank=True)
    item_number = models.PositiveSmallIntegerField(
        verbose_name="item_number", blank=True
    )
    date = models.DateField(verbose_name="date", blank=True)
    used_by = models.ForeignKey(
        Employee, blank=True, default=None, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"{self.device} - {self.price} $"
