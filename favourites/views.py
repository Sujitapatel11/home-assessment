from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from properties.models import Property
from .models import Favourite
from .serializers import FavouriteSerializer


class FavouriteListView(ListAPIView):
    serializer_class = FavouriteSerializer

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user).select_related('property')


class FavouriteAddView(APIView):
    def post(self, request):
        property_id = request.data.get('property')

        if not property_id:
            return Response({'error': 'property field is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            property_obj = Property.objects.get(pk=property_id)
        except Property.DoesNotExist:
            return Response({'error': 'Property not found.'}, status=status.HTTP_404_NOT_FOUND)

        favourite, created = Favourite.objects.get_or_create(
            user=request.user,
            property=property_obj
        )
        if not created:
            return Response({'error': 'Property is already in your favourites.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = FavouriteSerializer(favourite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FavouriteRemoveView(APIView):
    def delete(self, request, pk):
        favourite = Favourite.objects.filter(pk=pk, user=request.user).first()
        if not favourite:
            return Response({'error': 'Favourite not found.'}, status=status.HTTP_404_NOT_FOUND)

        favourite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
