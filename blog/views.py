from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import BlogPost, CommentBlogPost
from .forms import CommentBlogPostForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

import json

from django.http import HttpResponse
# from django.views import View
from django.contrib.contenttypes.models import ContentType

# Create your views here.

def blog_posts(request):
    blog_posts = BlogPost.objects.all()
    paginate_by = 2
    paginator = Paginator(blog_posts, paginate_by)

    page_number = request.GET.get('page')
    blog_posts= paginator.get_page(page_number)

    data = {
        'blog_posts' : blog_posts,
    }

    return render(request, 'blog/blog_posts.html', data)


def blog_post_detail(request, id):

    post = get_object_or_404(BlogPost, id=id)

    # List of active comments for this post
    comments = post.comments.filter(active=True, parent = None) #, year, month, day, post

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentBlogPostForm(request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = CommentBlogPost.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.post = post
            # save
            new_comment.save()
            #return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentBlogPostForm()

    count_comments = len(comments)
    gray_color = 'color: #212121;'

    context = {
        'post' : post,
        'comment_form': comment_form,
        'comments': comments,
        'count_comments' : count_comments,
        'gray_color' : gray_color,
    }

    return render(request, 'blog/single_blog_post.html', context)


def edit_comment(request, id):
    edit_comment = get_object_or_404(CommentBlogPost, id = id)
    # post_detail_self = BlogPost.objects.get(id = 1)

    if request.method == "POST":
        form = CommentBlogPostForm(request.POST, instance = edit_comment)
        if form.is_valid():
            CommentBlogPost.name = request.POST.get("name")
            CommentBlogPost.email = request.POST.get("email")
            CommentBlogPost.phone_number = request.POST.get("phone_number")
            CommentBlogPost.body = request.POST.get("body")
            edit_comment.save()
            return HttpResponseRedirect('/blog/')
    else:
        form = CommentBlogPostForm(instance = edit_comment)
    return render(request, 'blog/edit_comment.html', {'form' : form })


def delete_comment(request, id):
    try:
        delete_list = CommentBlogPost.objects.get(id=id)
        delete_list.delete()
        return HttpResponseRedirect("/blog/")
    except CommentBlogPost.DoesNotExist:
        return HttpResponseNotFound('<h2 class="alert alert-warning">Item not found</h2>')
