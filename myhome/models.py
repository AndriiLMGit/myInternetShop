from django.db import models


# Create your models here.

class RespondPost(models.Model):
    """docstring forBlogPost."""

    name_of_responders = models.CharField(max_length=20)
    text_of_responders = models.TextField()
    name_of_office_worker = models.CharField(max_length=10)
    avatat_image_of_responder = models.FileField(upload_to='responder_avatars/')


    def __str__(self):
        return self.name_of_responders