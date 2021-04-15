from django.db import models
from django.urls import reverse

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.

'-----------Мій власний код------------'
class BlogPost(models.Model):
    """docstring forBlogPost."""

    title_blog_post = models.CharField(max_length=20)
    description_blog_post = models.TextField()
    #slug = models.SlugField(max_length=250, null=True)
    published_at = models.DateTimeField()
    image_blog_post = models.FileField(upload_to='blog/')
    #slug = models.SlugField(max_length=50, unique=True, null=True)


    def __str__(self):
        return self.title_blog_post

    # def get_absolute_url(self):
    #     return reverse('blog_post_detail', args=[self.slug,])


class CommentBlogPost(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete = models.CASCADE)
    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete = models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
