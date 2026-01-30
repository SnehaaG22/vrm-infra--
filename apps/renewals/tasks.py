from celery import shared_task
from django.utils import timezone

@shared_task
def renewal_due_reminder():
    from .models import Renewal
    from apps.notifications.models import Notification

    today = timezone.now().date()

    for r in Renewal.objects.filter(due_date__lte=today):
        r.status = "OVERDUE"
        r.save()

        Notification.objects.create(
            org_id=r.org_id,
            user_id=1,
            type="RENEWAL_DUE",
            message="Vendor renewal overdue"
        )
