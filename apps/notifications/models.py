from django.db import models

class Notification(models.Model):
    org_id = models.IntegerField()
    user_id = models.IntegerField()
    type = models.CharField(max_length=50)
    message = models.TextField()
    status = models.CharField(max_length=20, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification {self.id} - {self.type}"
