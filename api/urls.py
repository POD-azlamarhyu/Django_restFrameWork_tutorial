from rest_framework import routers
from .views import TodoViewSet
from . import views
from django.urls import include,path
router = routers.DefaultRouter()
router.register(r'todo',TodoViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
