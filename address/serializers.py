from rest_framework import serializers

from users.serializer import UserSerializer


class CreateAddressSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    street = serializers.CharField()
    house_number = serializers.IntegerField()
    city = serializers.CharField()
    state = serializers.CharField()
    cep = serializers.CharField()
    country = serializers.CharField()
    user = UserSerializer(read_only=True)


class UpdateAddressSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    street = serializers.CharField(required=False)
    house_number = serializers.IntegerField(required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    cep = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    user = UserSerializer(read_only=True)
