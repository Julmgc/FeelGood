from rest_framework.permissions import BasePermission


class AdminGetPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            if request.user.is_admin:
                return True
            return False
        if request.method == "POST":
            if not request.user.is_admin:
                return True

        return False
