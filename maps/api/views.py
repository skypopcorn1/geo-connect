import itertools
from django.db.models import Sum
from rest_framework.generics import (
	ListAPIView,
	)
from rest_framework.parsers import (MultiPartParser, FormParser)
from rest_framework.response import Response
from maps.models import Map
from .serializers import (
	MapListSerializer,
	)

class MapDetailAPIView(ListAPIView):
	queryset = Map.objects.all()#values('description').annotate(Sum('rotation'))
	serializer_class = MapListSerializer
