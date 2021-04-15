from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('responds', views.responds, name="responds"),
    path('quickview', views.quickview, name="quickview"),
]
