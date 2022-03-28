from rest_framework import serializers
from . models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid','email','password','first_name','last_name', 'is_seller','is_admin','cpf','birthdate','is_active']
        read_only_fields = ['is_active']
        extra_kwargs = {'password':{'write_only':True}}

        
        

    def create(self, validated_data):
       

        user = User.objects.create_user(**validated_data)

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid','email','password','first_name','last_name', 'is_seller','is_admin','cpf','birthdate','is_active']
        extra_kwargs = {'password':{'write_only':True,'required':False}, 'is_active':{'required':False}}

   
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        if 'is_active' in validated_data:
            instance.is_active = validated_data.get('is_active', instance.is_active)    
            
        instance.save()
        return instance
    

  
