from django.urls import path
from Auth.Filter import views

urlpatterns = [
    path("filter/user", views.GetUsers.as_view()),
]
