

# Django
from django.contrib import admin


# Models
from .models import Channel



@admin.register(Channel)
class CannelAdmin(admin.ModelAdmin):
    pass