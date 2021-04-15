from django.urls import path
from . import views

from .models import BlogPost, CommentBlogPost

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.blog_posts, name="blog_posts"),
    path('<int:id>', views.blog_post_detail, name="blog_post_detail"),
    path('<int:id>/edit_comment', views.edit_comment, name="edit_comment"),
    path('<int:id>/delete_comment', views.delete_comment, name="delete_comment"),

]
