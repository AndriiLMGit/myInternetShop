from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_posts, name="blog_posts"),
    path('<int:id>', views.blog_post_detail, name="blog_post_detail"),
    path('<int:id>/edit_comment', views.edit_comment, name="edit_comment"),
    path('<int:id>/delete_comment', views.delete_comment, name="delete_comment"),
]
