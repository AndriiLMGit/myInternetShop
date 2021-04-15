from django.urls import path
from covid19 import views

urlpatterns = [
    path('', views.covid19, name="covid19"),

]
