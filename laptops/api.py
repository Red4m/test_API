from rest_framework import viewsets

from laptops.models import Laptops
from laptops.serializers import LaptopListSerializer


class LaptopModelViewSet(viewsets.ModelViewSet):
    serializer_class = LaptopListSerializer
    queryset = Laptops.objects.all()
