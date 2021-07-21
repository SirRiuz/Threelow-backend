
# Django
from django.contrib import admin

# Models
from .models import Reports


@admin.register(Reports)
class ReportAdmin(admin.ModelAdmin):
    pass