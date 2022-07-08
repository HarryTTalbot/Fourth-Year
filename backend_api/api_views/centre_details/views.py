from rest_framework import viewsets
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response

from .serializers import *
from .models import *

class CenterDetailsViewSet(viewsets.ViewSet):
    """
    Provides API functionality for managing center details.
    """
    pagination_class = None

    serializer_class = CenterDetailsSerializer

    @extend_schema(responses={200: CenterDetailsSerializer(many=False)})
    @ action(methods=['get'], detail=False, name="Get Center Details", url_path="", url_name="")
    def fetch(self, request):
        try:
            details = CenterDetails.objects.all()[0]
            serializer = CenterDetailsSerializer(
                instance=details, many=False)
            return Response(serializer.data, status=200)
        except:
            return Response("Center details have not been set", status=404)

    @extend_schema(request=CenterDetailsSerializer(many=False))
    def create(self, request):
        serializer = CenterDetailsSerializer(
            data=request.data, many=False)
        if serializer.is_valid():
            address = Address(line_one=serializer.validated_data['address']['line_one'],
                                     line_two=serializer.validated_data['address']['line_two'],
                                     line_three=serializer.validated_data['address']['line_three'],
                                     city_town=serializer.validated_data['address']['city_town'],
                                     province_district=serializer.validated_data[
                                         'address']['province_district'],
                                     post_code=serializer.validated_data['address']['post_code'],
                                     country=serializer.validated_data['address']['country'])

            details = CenterDetails(name=serializer.validated_data['name'],
                                           phone_number=serializer.validated_data['phone_number'],
                                           address=address)
            address.save()
            details.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
