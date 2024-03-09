from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Apps.urls")),
    path("api/", include("restAPI.urls")),
    path("Auth/", include("Auth.urls")),
    path("permisson/", include("Auth.Permissions.urls")),
    path("routers/", include("Auth.Router.urls")),
    path("filtering/", include("Auth.Filter.urls")),
]
