from django.urls import re_path

from apps.registration import views

urlpatterns = [
    re_path(r'^register_modal', views.register_modal),
    re_path(r'^register', views.register),
]
