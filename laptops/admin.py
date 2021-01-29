from django.contrib import admin

from laptops.models import Laptops


@admin.register(Laptops)
class LaptopAdmin(admin.ModelAdmin):
    list_display = (
        "device",
        "price",
        "team",
    )
