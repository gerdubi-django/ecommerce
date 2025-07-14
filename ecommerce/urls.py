from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("store.urls")),
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("users/", include("users.urls")),
]
