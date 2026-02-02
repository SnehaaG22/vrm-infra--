from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# ---------------- Evidence Model ----------------
class EvidenceFile(models.Model):
    org_id = models.IntegerField(null=True, blank=True)
    assessment_id = models.IntegerField(null=True, blank=True)
    question_id = models.IntegerField(null=True, blank=True)
    file_url = models.URLField()
    uploaded_by = models.IntegerField(null=True, blank=True)  # keeps your half-completed logic safe
    expiry_date = models.DateField(null=True, blank=True)
    file_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Evidence {self.id}"

# ---------------- Notification Model ----------------
class Notification(models.Model):
    org_id = models.IntegerField()
    user_id = models.IntegerField()
    type = models.CharField(max_length=50)
    message = models.TextField()
    status = models.CharField(max_length=20, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification {self.id} - {self.type}"
