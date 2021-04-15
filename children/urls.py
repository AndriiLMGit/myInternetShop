from django.urls import path
from . import views

urlpatterns = [
    path('', views.children, name="children"),
    path('<int:id>', views.children_view, name="children_view"),
]
