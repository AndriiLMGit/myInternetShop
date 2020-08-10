from .models import CommentBlogPost
from django.forms import ModelForm



class CommentBlogPostForm(ModelForm):

    class Meta:
        model = CommentBlogPost
        fields = ('name', 'email', 'phone_number', 'body' )
        
