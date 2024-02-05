from rest_framework.routers import DefaultRouter
from apps.notification.api.views.notification_viewset import NotificationsViewSet



router = DefaultRouter()
router.register(r'list',NotificationsViewSet, basename = 'list')





urlpatterns = router.urls 