from django.db.models import Sum
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from src.filters import EmployeeFilter
from src.models import Employee, Department
from src.paginator import EmployeePagination
from src.permissions import DepartmentPermission
from src.serializers import EmployeeReadSerializer, DepartmentReadSerializer, DepartmentListReadSerializer


class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeReadSerializer
    filterset_class = EmployeeFilter
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = EmployeePagination
    parser_classes = [FormParser, MultiPartParser]


class DepartmentView(ModelViewSet):
    queryset = Department.objects.prefetch_related('employees').all()
    serializer_class = DepartmentReadSerializer
    permission_classes = [DepartmentPermission]

    @swagger_auto_schema(responses={200: openapi.Response('', DepartmentListReadSerializer)})
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        employees_count = 0
        employees_total_salary = 0

        for i in queryset:
            employees_count += len(i.employees.all())
            employees_total_salary += i.employees.all().aggregate(total_salary=Sum('salary'))['total_salary'] or 0

        data = {
            "employees_count": employees_count,
            "employees_total_salary": employees_total_salary,
            "items": serializer.data
        }

        return Response(data)
