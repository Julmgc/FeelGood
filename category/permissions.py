from rest_framework.permissions import BasePermission


class CanCreateCategory(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous == True: return False
        if request.method == 'POST':
            if request.user.is_admin == True:
                return True
            return False
        
        return True

class CanGetCategory(BasePermission):
    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True
        else:
            if request.user.is_admin == True:
                return True
            return False