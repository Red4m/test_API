from rest_framework import serializers
from laptops.models import Laptops


class LaptopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptops
        fields = "__all__"
