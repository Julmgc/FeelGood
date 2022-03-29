from rest_framework.permissions import BasePermission


class AdminAndSellerUser(BasePermission):
    def has_permission(self, request, view):

        try:
          
            if request.user.is_admin or request.user.is_seller:
                return True
        except AttributeError:
            return False

        return False