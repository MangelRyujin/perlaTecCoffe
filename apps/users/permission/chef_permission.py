from rest_framework import permissions

class ChefGroupPermission(permissions.BasePermission):
    message = 'Chef access only.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='chef').exists()