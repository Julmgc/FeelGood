from rest_framework.permissions import BasePermission


class BuyerPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_admin or request.user.is_seller:
            return False
        return True
