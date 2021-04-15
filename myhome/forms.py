from django.forms import ModelForm
from .models import RespondPost


class RespondPostForm(ModelForm):

    class Meta:
        model = RespondPost
        fields = '__all__'