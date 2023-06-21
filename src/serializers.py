from rest_framework import serializers

from src.models import Employee, Department


class EmployeeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class DepartmentReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentListReadSerializer(serializers.Serializer):
    employees_count = serializers.IntegerField()
    employees_total_salary = serializers.IntegerField()
    items = DepartmentReadSerializer(many=True)
