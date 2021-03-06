from rest_framework.permissions import BasePermission

class AdminUser(BasePermission):
    def has_permission(self, request, view):

        if request.method == 'POST':
            return True
        try:

            if request.user.is_admin:
                return True
        except AttributeError:
            return False

        return False


class AdminAndUser(BasePermission):
    def has_permission(self, request, view):

        if request.method == 'PATCH':
            return True
        try:

            if request.user.is_admin:
                return True
        except AttributeError:
            return False

        return False


class AdminSale(BasePermission):
    def has_permission(self, request, view):

        if request.method == 'GET':
            return True
        try:

            if request.user.is_admin:
                return True
        except AttributeError:
            return False

        return False


class ClientOrSellerProductReview(BasePermission):
    def has_permission(self, request, view):

        if request.method == 'GET':
            return True
        try:

            if not request.user.is_admin:
                return True
        except AttributeError:
            return False

        return False


