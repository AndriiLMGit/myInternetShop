from django.urls import path
from . import views

urlpatterns = [
    path('', views.bags, name="bags"),
    path('<int:id>', views.bags_detail, name="bags_detail"),
    path('<int:id>/edit_comment', views.edit_comment, name="edit_comment"),
    path('<int:id>/delete_comment', views.delete_comment, name="delete_comment"),
]
