from django.shortcuts import render
from rest_framework.views import APIView
from Auth.models import User
from rest_framework.response import Response
from rest_framework.request import Request
from Auth.serializers import GetUserSerializers
from rest_framework import status


class GetUsers(APIView):

    def get(self, request: Request):
        data = User.objects.all()
        serializers = GetUserSerializers(data, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
