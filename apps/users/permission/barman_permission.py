from rest_framework import permissions

class BarmanGroupPermission(permissions.BasePermission):
    message = 'Barman access only.'
    
    def has_permission(self, request, view):
        return request.user.groups.filter(name='barman').exists()