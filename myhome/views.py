from django.shortcuts import render
from blog.views import blog_posts
from blog.models import BlogPost
from blog.views import blog_post_detail
from .forms import RespondPostForm
from .models import RespondPost
from django.http import HttpResponseRedirect

# Create your views here.
def responds(request):
    if request.method == 'POST':
        form_respond = RespondPostForm(request.POST, request.FILES)
        if form_respond.is_valid():
            name_of_responders = form_respond.cleaned_data['name_of_responders']
            text_of_responders = form_respond.cleaned_data['text_of_responders']
            name_of_office_worker = form_respond.cleaned_data['name_of_office_worker']
            avatat_image_of_responder = form_respond.cleaned_data['avatat_image_of_responder']
            form_respond.save()
            return HttpResponseRedirect('/')
    else:
        form_respond = RespondPostForm()
    
    context = {
        'form_respond' : form_respond,
    }

    return render(request, 'myhome/leave_respond.html', context)

def index(request):
    queryset_blog_posts = BlogPost.objects.all()
    form_respond_items = RespondPost.objects.all()

    data = {
        'queryset_blog_posts' : queryset_blog_posts,
        'form_respond_items' : form_respond_items,
        
    }
    return render(request, 'myhome/index.html', data)

def quickview(request):
    return render(request, "myhome/quickview.html", {})