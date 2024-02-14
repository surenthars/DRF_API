from django.urls import path
from .views import Get_view

urlpatterns = [
    path("ONE", Get_view),
]
