from django.contrib import admin
from .models import EvidenceFile

@admin.register(EvidenceFile)
class EvidenceFileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in EvidenceFile._meta.fields]
    search_fields = [f.name for f in EvidenceFile._meta.fields]
