from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from .views import NotificationsViewSet, index
router = routers.SimpleRouter()
router.register(r'panel', NotificationsViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^panel$', index, name='register')
]
