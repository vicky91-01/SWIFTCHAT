# swiftchat/urls.py
from django.contrib import admin
from django.urls import path, include
from swiftchat import views as swiftchat_views  # Explicit import

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("chatapp.urls")),
]
