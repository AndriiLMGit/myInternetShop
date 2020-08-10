from django.contrib import admin
from .models import BlogPost
from .models import CommentBlogPost

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body',)


admin.site.register(BlogPost)

admin.site.register(CommentBlogPost, CommentAdmin)
