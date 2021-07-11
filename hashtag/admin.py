

# Django
from django.contrib import admin


# Models
from .models import HashTag


@admin.register(HashTag)
class TagAdmin(admin.ModelAdmin):
    pass