from re import I
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView
from rest_framework.response import Response
from users.models import User
from users.serializer import UserSerializer,LoginSerializer,UpdateSerializer
from users.permissions import AdminUser,AdminAndUser
from rest_framework.authentication import TokenAuthentication,authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import exception_handler

# Create your views here.
class UserView(ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer
   

class UserListOneView(RetrieveUpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminAndUser]

    queryset = User.objects.all()
    serializer_class = UpdateSerializer
    lookup_url_kwarg = 'user_id'
    

   

class LoginView(APIView):
    def post(self,request):

        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        email = request.data['email']
        password = request.data['password']
        user = authenticate(email=email, password=password)

        if user :
            token = Token.objects.get_or_create(user=user)[0]
            return Response({'token':token.key}, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_401_UNAUTHORIZED)


