from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.role == 'admin' or request.user.is_staff)

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.role == 'admin' or request.user.is_staff)