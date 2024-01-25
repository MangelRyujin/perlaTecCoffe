from rest_framework.routers import DefaultRouter
from apps.restaurant.api.views.restaurant_viewset import RestaurantViewSet



router = DefaultRouter()
router.register(r'locals',RestaurantViewSet, basename = 'locals')





urlpatterns = router.urls 