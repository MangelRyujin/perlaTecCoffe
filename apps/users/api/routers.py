from rest_framework.routers import DefaultRouter
from apps.users.api.views.userRegister_view import RegisterViewSet



router = DefaultRouter()
router.register(r'users',RegisterViewSet, basename = 'users')





urlpatterns = router.urls 