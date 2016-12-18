from django.contrib import admin

from .models import Event

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'category', 'date');
    list_filter = ('city', 'category', 'date');
