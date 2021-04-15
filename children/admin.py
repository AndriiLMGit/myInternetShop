from django.contrib import admin

from children.models import ChildrenThing, ChildrenThingComment

# Register your models here.
admin.site.register(ChildrenThing)

admin.site.register(ChildrenThingComment)