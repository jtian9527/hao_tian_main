from django.conf.urls import url, include
from demo.api import view
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^list', view.list),
    url(r'^create_demo', view.create_demo),
]