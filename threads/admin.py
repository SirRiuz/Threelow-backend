

# Django
from django.contrib import admin


# Models
from .models import Thread


@admin.register(Thread)
class ThreadsAdmin(admin.ModelAdmin):
    list_display = [ 'id','owner','text' ]
    list_filter = [ 'owner' ]