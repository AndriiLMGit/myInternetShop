from django.urls import path
from finance import views

urlpatterns = [
    path('', views.main_finance, name="main_finance"),
    

]
