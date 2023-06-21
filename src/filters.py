import django_filters
from src.models import Employee


class EmployeeFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    department = django_filters.NumberFilter()

    class Meta:
        model = Employee
        fields = ['department', 'last_name']
