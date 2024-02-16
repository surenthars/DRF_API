from django.urls import path
from . import views

urlpatterns = [
    path("one/user", views.first_view),
]
