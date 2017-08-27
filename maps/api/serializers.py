from rest_framework.serializers import ModelSerializer
from maps.models import Map

class MapListSerializer(ModelSerializer):
    class Meta:
        model = Map
        fields = (
            'x',
            'y',
            'z',
            'x_origin',
            'y_origin',
            'x_extent',
            'y_extent',
            'x_mesh_size',
            'y_mesh_size',
            'rotation',
            'description',
            'last_updated',
            )
