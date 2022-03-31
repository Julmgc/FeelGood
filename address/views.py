from rest_framework.views import APIView
from .serializers import CreateAddressSerializer, UpdateAddressSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Address
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class AddressView(APIView):

    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]

    def put(self, request):
        if request.user.is_anonymous:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = CreateAddressSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        address = Address.objects.get_or_create(**serializer.validated_data)
        user = request.user

        user.address = address[0]
        user.save()

        return Response(CreateAddressSerializer(address[0]).data, status=status.HTTP_200_OK)

    def patch(self, request):
        if request.user.is_anonymous:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
            
        serializer = UpdateAddressSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        if request.user.address == None:
            return Response({"detail": "Address not found."}, status=status.HTTP_404_NOT_FOUND)
        address = Address.objects.filter(
            id=request.user.address.id).update(**serializer.validated_data)
        

        user = request.user
        filtered_address = Address.objects.get(id=request.user.address.id)

        user.address = filtered_address

        user.save()

        return Response(UpdateAddressSerializer(filtered_address).data, status=status.HTTP_200_OK)
