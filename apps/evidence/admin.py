from django.contrib import admin
from .models import EvidenceFile

@admin.register(EvidenceFile)
class EvidenceFileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in EvidenceFile._meta.fields]
<<<<<<< HEAD
    search_fields = [f.name for f in EvidenceFile._meta.fields]
=======
    search_fields = [f.name for f in EvidenceFile._meta.fields]
>>>>>>> d271ac02bcff173701a74d6a74264cec6e1e213f
