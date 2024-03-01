from .models import Client
from .serializers import ClientSerializers
from rest_framework.views import APIView
from rest_framework import generics, mixins, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.decorators import permission_classes, api_view

# custom user permission

from .permissions import ReadOnly, AuthorOrReadonly


class ClientViews(APIView):
    serializer_class = ClientSerializers
    permission_classes = [AuthorOrReadonly]

    def get(self, request: Request):
        clientdata = Client.objects.all()
        serialzer = self.serializer_class(clientdata, many=True)
        return Response(
            serialzer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request: Request):
        postdata = request.data
        serializer = self.serializer_class(data=postdata)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


# @permission_classes([AllowAny])-->Its Allow All token valid or not its not checking
# @permission_classes([ISAuthenticated])-->Its Allow only Authenticated User Only
# @permission_classes([IsAdminUser]) -->Admin Can only Access the Api
# @permission_classes([IsAuthenticatedOrReadOnly])--> when i credential provided its perform all action not provided its working get only
# importentthing configure the steeing file default permission


@api_view(http_method_names=["GET"])
@permission_classes([IsAdminUser])
def HandlegetClient(request: Request):
    clientdata = Client.objects.all()
    serialzer = ClientSerializers(clientdata, many=True)
    return Response(
        serialzer.data,
        status=status.HTTP_200_OK,
    )
