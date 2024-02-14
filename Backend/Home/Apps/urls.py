from django.urls import path
from .views import Get_view, get_home, get_modelInstance

urlpatterns = [
    path("check", Get_view),
    path("home", get_home),
    path("modelinstance", get_modelInstance),
]
