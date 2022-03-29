from rest_framework.permissions import BasePermission


class GetPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return False


class AdminPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        if request.user.is_admin:
            return True
        return False
