from django.shortcuts import render
from django.http import JsonResponse
import json


def Get_view(request, *args, **kwargs):
    body = request.body

    # data = {"name": "Surenthar", "Age": 21}
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print("GET", request.GET)
    print("POST", request.POST)
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    return JsonResponse(data)
