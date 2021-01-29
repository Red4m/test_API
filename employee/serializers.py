from rest_framework import serializers
from employee.models import Employee


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
