from rest_framework.generics import ListAPIView
from .models import Property
from .serializers import PropertySerializer


class PropertyListView(ListAPIView):
    queryset = Property.objects.all().order_by('-created_at')
    serializer_class = PropertySerializer
