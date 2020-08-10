from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import BlogPost, CommentBlogPost
from .forms import CommentBlogPostForm
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def blog_posts(request):
    blog_posts = BlogPost.objects.all()

    context = {
        'blog_posts' : blog_posts,
    }

    return render(request, 'blog/blog_posts.html', context)


def blog_post_detail(request, id):

    post = get_object_or_404(BlogPost, id = id)

    # List of active comments for this post
    comments = post.comments.filter(active=True, parent__isnull=True) #, year, month, day, post

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
                    replay_comment.parent_obj = parent_obj

                    #replay_comment.save()
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()

            #return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentBlogPostForm()

    count_comments = len(comments)

    context = {
        'post' : post,
        'comment_form': comment_form,
        'comments': comments,
        'count_comments' : count_comments,
    }

    return render(request, 'blog/single_blog_post.html', context)


def edit_comment(request, id):
    edit_comment = get_object_or_404(CommentBlogPost, id = id)

    post_detail_self = BlogPost.objects.get(id = 1)

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
    return render(request, 'blog/edit_comment.html', {'form' : form})


def delete_comment(request, id):
    try:
        delete_list = CommentBlogPost.objects.get(id=id)
        delete_list.delete()
        return HttpResponseRedirect("/blog/")
    except CommentBlogPost.DoesNotExist:
        return HttpResponseNotFound('<h2 class="alert alert-warning">Item not found</h2>')
