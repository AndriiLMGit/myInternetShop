from django.contrib import admin
from bags.models import Bag, CommentBag

# Register your models here.
admin.site.register(Bag)


class CommentBagAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'bag_post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(CommentBag, CommentBagAdmin)