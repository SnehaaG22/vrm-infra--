from django.contrib import admin
from .models import Renewal

@admin.register(Renewal)
class RenewalAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Renewal._meta.fields]
    search_fields = [f.name for f in Renewal._meta.fields]
