from django.conf.urls import url, include
from demo.replay import view
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
]