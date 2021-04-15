from django.shortcuts import render, get_object_or_404, redirect
from children.models import ChildrenThing, ChildrenThingComment
from .forms import ChildrenThingCommentForm

# Create your views here.

def children(request):
    children_things = ChildrenThing.objects.all()

    context = {
        'children_things' : children_things,
    }

    return render(request, 'children/children.html', context)


def children_view(request, id):

    children_thing = get_object_or_404(ChildrenThing, id = id)

     # List of active comments for this post
    comments = children_thing.comments.filter(active=True, parent = None) #, year, month, day, post

    if request.method == 'POST':
        # A comment was posted
        comment_form = ChildrenThingCommentForm(request.POST)
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
                parent_obj = ChildrenThingComment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.children_thing = children_thing
            # save
            new_comment.save()
            #return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = ChildrenThingCommentForm()

    context = {
        'children_thing' : children_thing,
        'comment_form' : comment_form,
        'comments' : comments,
    }

    return render(request, 'children/children_view.html', context)