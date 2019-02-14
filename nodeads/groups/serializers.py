from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Vehicle, VehicleType


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'picture', 'name', 'model_name',
                  'description', 'date', 'verified', 'owner', 'types')


class VehicleTypeNested(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(
        source='parent',
        read_only=True
    )

    class Meta:
        model = VehicleType

        fields = (
            'id',
            'name',
            'description',
            # 'level',
            # 'tree_id',
            'parent_id',
        )


class VehicleTypeSerializer(serializers.ModelSerializer):
    parent = VehicleTypeNested(read_only=True)

    descendant_count = serializers.SerializerMethodField()

    class Meta:
        model = VehicleType

        fields = (
            'id',
            'descendant_count',
            'name',
            'parent',
            'description',
            # 'level',
            # 'tree_id',
        )

    def get_descendant_count(self, obj):
        return obj.get_descendant_count()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    vehicles = serializers.HyperlinkedRelatedField(
        many=True, view_name='vehicle-detail', read_only=True
    )

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'vehicles')
