from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import Product
from django.forms.models import model_to_dict


def Get_view(request, *args, **kwargs):
    body = request.body

    # data = {"name": "Surenthar", "Age": 21}
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print("GET", request.GET)  # ==>GET return <QueryDict: {}>
    print("POST", request.POST)  # ==>POST return <QueryDict: {}>
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    return JsonResponse(data)


def get_home(request):
    if request.method == "GET":
        print(request.method)
        productdata = Product.objects.all().order_by("?").first()
        data = {}
        if productdata:
            data["title"] = productdata.title
            data["content"] = productdata.content
            data["price"] = productdata.price
        # Serialization
        # model instance (productdata)
        # turn a python dict
        # return Json to my Client
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"message": "Method Not Allowed"}, safe=False)


def get_modelInstance(request):
    if request.method == "GET":
        productdata = Product.objects.all().order_by("?").first()
        data = {}
        if productdata:
            data = model_to_dict(productdata, fields=["title", "content"])
        return JsonResponse(data)
    else:
        return JsonResponse({"message": "Method Not Allowed"}, safe=False)
