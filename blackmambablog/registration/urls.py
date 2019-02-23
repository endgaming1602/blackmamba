from django.urls import include, path

from django.contrib.auth.views import (LoginView, LogoutView)

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]
