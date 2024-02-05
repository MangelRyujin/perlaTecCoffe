from django.contrib import admin
from apps.notification.models import Notification
from .models import Notification
# Register your models here.


admin.site.register(Notification)