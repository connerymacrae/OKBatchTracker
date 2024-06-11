from django.contrib import admin

# Register your models here.
from .models import Batch

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('brewer', 'name', 'description', 'date_brewed', 'starter_type')