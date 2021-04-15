from django.urls import path
from . import views

urlpatterns = [
    path('', views.men_main_view, name="men_main_view"),
    path('<int:id>', views.men_detail_view, name="men_detail_view"),

]
