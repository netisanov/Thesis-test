from rest_framework import routers
from src.views import EmployeeView, DepartmentView

router = routers.SimpleRouter()
router.register(r'employees', EmployeeView)
router.register(r'departments', DepartmentView)

urlpatterns = router.urls
