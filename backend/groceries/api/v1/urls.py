from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ItemViewSet, ListViewSet, RunViewSet

router = DefaultRouter()
router.register("item", ItemViewSet)
router.register("list", ListViewSet)
router.register("run", RunViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
