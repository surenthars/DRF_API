from django.urls import path
from Auth.Permissions import views

urlpatterns = [
    path("client", views.ClientViews.as_view()),
    path("function/client", views.HandlegetClient),
]
