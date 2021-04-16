from django.db import models
from django.db import IntegrityError

# Create your models here.
class Bag(models.Model):

    """docstring"""

    name_bag = models.CharField(max_length=20)
    description_bag = models.TextField(blank=True)
    price_bag = models.PositiveIntegerField()
    title_image = models.FileField(upload_to='bags/title/')
    detail_big_image = models.FileField(upload_to='bags/detail_bags_images/')
    detail_middle_image = models.FileField(upload_to='bags/detail_bags_images/')
    bag_published_at = models.DateTimeField()

    def __str__(self):
        return self.name_bag
    

class CommentBag(models.Model):
    bag_post = models.ForeignKey(Bag, related_name='comments_bag', on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    new_field = models.TextField(help_text = "new field for test")
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete = models.CASCADE)

    class Meta:
        ordering = ('created',)
