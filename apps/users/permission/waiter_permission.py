from rest_framework import permissions

class WaiterGroupPermission(permissions.BasePermission):
    message = 'Waiter access only.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='waiter').exists()