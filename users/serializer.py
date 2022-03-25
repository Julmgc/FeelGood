from rest_framework import serializers
from . models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid','email','password','first_name','last_name', 'is_seller','is_admin','cpf','birthdate']
        read_only_fields = ['is_active']
        extra_kwargs = {'password':{'write_only':True}}

        
        

    def create(self, validated_data):
       

        user = User.objects.create_user(**validated_data)

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()