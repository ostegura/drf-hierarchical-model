from django.urls import path, include
from rest_framework.routers import DefaultRouter
from groups import views


# creating a router and registering our viewsets with it
router = DefaultRouter()
router.register(r'vehicle', views.VehicleViewSet)
router.register(r'vehicletype', views.VehicleTypeViewSet)
router.register(r'groups', views.UserViewSet)


# API urls are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
