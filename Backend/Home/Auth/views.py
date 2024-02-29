from django.shortcuts import render
from .models import User
from rest_framework.permissions import IsAuthenticated
from .serializers import SignUpSerializers, GetUserSerializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

# Create your views here.


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializers
    permission_classes = []

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "User Has Been Created",
                "data": serializer.data,
                "status": status.HTTP_201_CREATED,
            }
            return Response(response)
        else:
            response = {
                "message": "Something Error Found",
                "data": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST,
            }
            return Response(response)


class LoginView(APIView):
    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        refresh = RefreshToken.for_user(user)

        tokens = {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }

        if user is not None:
            response = {
                "message": "Login Sucessfully",
                "token": tokens,
                "status": status.HTTP_200_OK,
            }
            return Response(response)
        else:
            response = {
                "message": "User Not Found",
                "status": status.HTTP_404_NOT_FOUND,
            }
            return Response(response)

    def get(self, request: Request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(data=content, status=status.HTTP_200_OK)


class GetUsers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        data = User.objects.all()
        serializers = GetUserSerializers(data, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
