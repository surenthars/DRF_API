from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Apps.urls")),
    path("api/", include("restAPI.urls")),
    path("Auth/", include("Auth.urls")),
    path("Posts/", include("Auth.Serializers_Relationship.urls")),
]
