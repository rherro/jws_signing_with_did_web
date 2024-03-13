from django.urls import path
from . import views

urlpatterns = [
    path('did.json', views.index)
]
