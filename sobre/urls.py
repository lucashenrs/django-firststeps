from django.urls import path
from . import views

urlpatterns = [
    path('', views.func_render)
]