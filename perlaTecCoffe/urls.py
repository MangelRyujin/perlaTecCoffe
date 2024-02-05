"""
URL configuration for perlaTecCoffe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.views.static import serve
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi 



schema_view = get_schema_view(
    openapi.Info(
        title = "PerlaTec Restaurant",
        default_version = "version 1.0",
        description = "PerlaTec Restaurant Public documentation",
        terms_of_service = "https://www.google.com/policies/terms/",
        contact = openapi.Contact(email ="mangelryujin@gmail.com"),
        License = openapi.License(name = "BSD License"),     
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path("admin/", admin.site.urls),
    path('restaurant/', include('apps.restaurant.api.routers')),
    path('products/', include('apps.products.api.routers')),
    path('orders/', include('apps.orders.api.routers')),
    path('kitchen/', include('apps.kitchen.api.routers')),
    path('accounts/', include('dj_rest_auth.urls')),
    re_path(r'^swagger(?P<format>\.json/\.yaml)$', schema_view.without_ui(cache_timeout=0), name = 'schema-json'),
    path('api-docs/', schema_view.with_ui('swagger',cache_timeout=0), name = 'schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0), name = 'schema-swagger-redoc'),
]


urlpatterns+=[
    re_path(r'^media/(?P<path>.*)$',serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]