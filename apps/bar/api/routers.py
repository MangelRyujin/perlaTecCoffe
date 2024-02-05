from rest_framework.routers import DefaultRouter
from apps.bar.api.views.bar_viewset import ItemsBarViewSet



router = DefaultRouter()
router.register(r'items-details',ItemsBarViewSet, basename = 'items-details')





urlpatterns = router.urls 