from rest_framework.routers import DefaultRouter
from apps.orders.api.views.orders_viewset import OrderViewSet



router = DefaultRouter()
router.register(r'details',OrderViewSet, basename = 'orders')





urlpatterns = router.urls 