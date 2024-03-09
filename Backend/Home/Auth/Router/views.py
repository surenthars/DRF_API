from django.shortcuts import render
from Auth.models import User
from Auth.serializers import GetUserSerializers, SignUpSerializers
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

"""
class Based Views 
-get()
-post()
-put()
-etc

Viewsets 
-.create()
-.list()
-.retrive()
"""


class PostViewSet(viewsets.ViewSet):
    def list(self, request: Request):
        user = User.objects.all()
        serializer = GetUserSerializers(instance=user, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrive(self, request: Request, pk=None):
        user = get_object_or_404(pk=pk)

        serailzer = GetUserSerializers(instance=user)

        return Response(data=serailzer.data, status=status.HTTP_200_OK)
