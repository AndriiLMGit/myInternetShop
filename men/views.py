from .models import TShirt
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.


def men_main_view(request):
    """
    docstring
    """
    query_set_tshirts = TShirt.objects.all()

    template_name = 'men/men_main_view.html'

    data = {
        'tshirts' : query_set_tshirts,
    }

    return render(request, template_name, data)


def men_detail_view(request, id):
    """
    docstring
    """
    men_thing = get_object_or_404(TShirt, id = id)
    template_name = "men/men_detail_view.html"

    data = {
        "men_thing" : men_thing,
    }

    return render(request, template_name, data)