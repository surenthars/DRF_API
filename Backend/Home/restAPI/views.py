from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Users


# inthis apiview is given python its considered takes django api views
@api_view(["GET"])
def first_view(request):
    """DRF APi View"""
    userdata = Users.objects.all().order_by("?").first()
    data = {}
    if userdata:
        data["userName"] = userdata.userName
        data["email"] = userdata.email
    return Response(data)
