
# Django
from django.contrib import admin


# Models
from .models import Reaction,ThreadReaction



@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = [ 'id','name','image' ]
    list_display_links = [ 'name' ]



@admin.register(ThreadReaction)
class REactionThreadAdmin(admin.ModelAdmin):
    list_display = [ 'id','ownerReaction','thread','reaction' ]
    list_display_links = [ 'id','ownerReaction','thread','reaction' ]
    list_filter = [ 'ownerReaction' ]



