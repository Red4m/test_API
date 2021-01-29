from rest_framework import viewsets

from employee.models import Employee
from employee.serializers import EmployeeListSerializer


class EmployeeModelViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeListSerializer
    queryset = Employee.objects.all()
