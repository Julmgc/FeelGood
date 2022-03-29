from rest_framework.permissions import BasePermission


class AdminPermission(BasePermission):
    def has_permission(self, request, view):


        if request.method == 'GET':
            return True
        try:
          
            if request.user.is_admin:
                return True
        except AttributeError:
            return False

        return False