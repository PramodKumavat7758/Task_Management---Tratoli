from inspect import stack

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


User = get_user_model()
class RegisterUser(APIView):

    def post(self,request):
        data = request.data
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            password=make_password(data['password'])

        )
        return Response({"message":"User Created...!"}, status = status.HTTP_201_CREATED)

class LogoutView(APIView):
    def post(self,request):
        return Response({"message": "Logout Success..!"}, status = status.HTTP_200_OK)