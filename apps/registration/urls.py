from django.urls import re_path

from apps.registration import views

urlpatterns = [
    re_path(r'^register', views.register_request, name="register")
]
