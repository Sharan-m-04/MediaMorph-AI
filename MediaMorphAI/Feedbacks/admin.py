from django.contrib import admin
from .models import Feedback

# Register your models here.
@admin.register(Feedback)
class UserFeedbacks(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email')
