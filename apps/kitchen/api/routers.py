from rest_framework.routers import DefaultRouter
from apps.kitchen.api.views.kitchen_viewset import ItemsKitchenViewSet



router = DefaultRouter()
router.register(r'items-details',ItemsKitchenViewSet, basename = 'items-details')





urlpatterns = router.urls 