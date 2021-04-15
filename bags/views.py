from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.db.models import Count
from bags.models import Bag, CommentBag
from bags.forms import CommentBagForm
from django.db import IntegrityError


# Create your views here.
def bags(request):

    list_bags = Bag.objects.all()
    
    context_bags_all = {
        'list_bags' : list_bags,
    }
    return render(request, 'bags/bags_all.html', context_bags_all)



def bags_detail(request, id):

    bag_post = get_object_or_404(Bag, id = id)

    #  List of active comments for this post
    comments_bag = bag_post.comments_bag.filter(active=True, parent = None)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentBagForm(data=request.POST)
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
                parent_obj = CommentBag.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.bag_post = bag_post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentBagForm()

    context_bag_detail = {
        'bag_post' : bag_post,
        'comments_bag' : comments_bag,
        'comment_form': comment_form,
    }

    return render(request, 'bags/bags_detail.html', context_bag_detail)


def edit_comment(request, id):

    edit_comment = get_object_or_404(CommentBag, id = id)

    id_comment = CommentBag.objects.get(id = id)

    url_edit_comment = '/bags/'

    if request.method == "POST":
        form = CommentBagForm(request.POST, instance = edit_comment)
        if form.is_valid():
            CommentBag.name = request.POST.get("name")
            CommentBag.email = request.POST.get("email")
            CommentBag.phone_number = request.POST.get("phone_number")
            CommentBag.body = request.POST.get("body")
            edit_comment.save()
            return redirect(url_edit_comment)
    else:
        form = CommentBagForm(instance = edit_comment)
    return render(request, 'blog/edit_comment.html', {'form' : form })


def delete_comment(request, id):
    try:
        delete_list = CommentBag.objects.get(id=id)
        delete_list.delete()
        return HttpResponseRedirect("/bags/")
    except CommentBag.DoesNotExist:
        return HttpResponseNotFound('<h2 class="alert alert-warning">Item not found</h2>')