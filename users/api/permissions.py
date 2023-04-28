from rest_framework.permissions import BasePermission



class IsCreator(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_creator)
    
class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)