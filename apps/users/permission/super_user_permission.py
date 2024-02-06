from rest_framework import permissions

class IsSuperUserOrAdmin(permissions.BasePermission):
    """
    Permite el acceso a superusuarios y a usuarios autenticados.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='administrator').exists() or request.user.is_superuser 