from django.db import models

# Create your models here.
class MenCategory(models.Model):
    name_category = models.CharField(max_length=50)

    def __str__(self):
        return self.name_category


class TShirt(models.Model):
    """
    docstring
    """
    COLOR_OF_TSHIRTS = [
        ('Red' , 'Red'),
        ('Blue' , 'Blue'),
        ('White' , 'White'),
        ('Yellow' , 'Yellow'),
        ('Green' , 'Green'),
        ('Purple' , 'Purple'),
    ]
    category = models.ForeignKey(MenCategory, on_delete=models.CASCADE)
    name_brand = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=50, choices=COLOR_OF_TSHIRTS, default='White')
    image_thumbnail = models.FileField(upload_to='men/t_shirts/thumbnail/')
    text = models.TextField(null=True)

    def __str__(self):
        return self.name_brand

    