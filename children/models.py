from django.db import models

# Create your models here.


class ChildrenThing(models.Model):
    """
    docstring
    """
    name_children_thing = models.CharField(max_length=30)
    new_price_children_thing = models.PositiveIntegerField()
    old_price_children_thing = models.PositiveIntegerField()
    describe_children_thing = models.TextField()
    front_image_children_thing = models.FileField(upload_to='children/title')
    back_image_children_thing = models.FileField(upload_to='children/title')
    big_detail_image_children_thing = models.FileField(upload_to='children/detail')
    middle_1_detail_image_children_thing = models.FileField(upload_to='children/detail')
    middle_2_detail_image_children_thing = models.FileField(upload_to='children/detail')
    children_published_at = models.DateTimeField()

    def __str__(self):
        return self.name_children_thing


class ChildrenThingComment(models.Model):
    children_thing = models.ForeignKey(ChildrenThing, related_name='comments', on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete = models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.children_thing)
    
