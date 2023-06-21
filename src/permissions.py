from rest_framework.permissions import BasePermission


class DepartmentPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True  # Allow unauthenticated access to the 'list' method
        return request.user.is_authenticated