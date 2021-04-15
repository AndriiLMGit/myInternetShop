from .models import CommentBag
from django.forms import ModelForm



class CommentBagForm(ModelForm):

    class Meta:
        model = CommentBag
        fields = ('name', 'email', 'phone_number', 'body')