from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.notification.api.serializers.notification_serializer import NotificationsSerializer
from apps.notification.models import Notification


    


class NotificationsViewSet(viewsets.GenericViewSet):
    serializer_class= NotificationsSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self,user = None):
        if user is None:
            return None
        return self.get_serializer().Meta.model.objects.filter(user=user).order_by('-date','-time')

    
    #method list all notifications with user id
    def list(self, request):
        notifications = self.get_queryset(request.user.id)
        if notifications:
            notifications_serializers = self.serializer_class(notifications, many=True)
            return Response(notifications_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existen notificaciones'}, status= status.HTTP_404_NOT_FOUND)
    
    
    