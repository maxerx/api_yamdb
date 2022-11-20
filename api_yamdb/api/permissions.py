from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            if request.user.is_anonymous:
                return False
            else:
                return request.user.role == 'admin' or request.user.is_staff
        else:
            return True

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.role == 'admin' or request.user.is_staff)