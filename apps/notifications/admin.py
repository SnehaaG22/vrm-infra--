from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Notification._meta.fields]
    search_fields = [f.name for f in Notification._meta.fields]
