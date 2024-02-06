from rest_framework import permissions

class AdministratorGroupPermission(permissions.BasePermission):
    message = 'Administrator access only.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='administrator').exists()