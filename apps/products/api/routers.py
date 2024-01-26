from rest_framework.routers import DefaultRouter
from apps.products.api.views.products_viewset import ProductsViewSet



router = DefaultRouter()
router.register(r'presentation',ProductsViewSet, basename = 'products')





urlpatterns = router.urls 