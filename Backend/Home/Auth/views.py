from django.shortcuts import render
from .models import User
from .serializers import SignUpSerializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

# Create your views here.


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializers

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
