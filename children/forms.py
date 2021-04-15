from django.forms import ModelForm
from .models import ChildrenThingComment


class ChildrenThingCommentForm(ModelForm):

    class Meta:
        model = ChildrenThingComment
        fields = ('name', 'email', 'phone_number', 'body' )
        


