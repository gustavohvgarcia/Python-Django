from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("funcionarios.urls")),
    path("admin/", admin.site.urls),
]
