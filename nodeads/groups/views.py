from groups.models import Vehicle, VehicleType
from groups.serializers import VehicleSerializer, VehicleTypeSerializer
from groups.serializers import UserSerializer
from groups.permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import permissions


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.filter(verified=True)
    # queryset = Vehicle.objects.all()

    serializer_class = VehicleSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'vehicles': reverse('vehicles-list', request=request, format=format)
    })
