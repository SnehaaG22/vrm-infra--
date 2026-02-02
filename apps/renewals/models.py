from django.db import models
from django.conf import settings

class Renewal(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('OVERDUE', 'Overdue'),
    ]
    
    name = models.CharField(max_length=255, blank=True, null=True)  # optional
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')
    due_date = models.DateField()
    org_id = models.IntegerField()
    vendor_id = models.IntegerField(null=True, blank=True)  # if you need it
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Renewal {self.id} - {self.status}"
