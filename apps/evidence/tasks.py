from celery import shared_task
from django.utils import timezone
from datetime import timedelta

from .models import EvidenceFile
from apps.notifications.models import Notification


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=30, retry_kwargs={'max_retries': 3})
def evidence_expiry_reminder(self):
    """
    Notify when evidence is expiring in 30 / 15 / 7 days
    """

    today = timezone.now().date()

    for days in [30, 15, 7]:
        target = today + timedelta(days=days)

        evidences = EvidenceFile.objects.filter(expiry_date=target)

        for e in evidences:
            Notification.objects.create(
                org_id=e.org_id,
                user_id=e.uploaded_by,
                type="EVIDENCE_EXPIRY",
                message=f"Evidence expires in {days} days",
                status="pending",
            )


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=30, retry_kwargs={'max_retries': 3})
def renewal_due_reminder(self):
    """
    Mark expired evidence as overdue (temporary MVP logic)
    Later replace EvidenceFile with Renewal model
    """

    today = timezone.now().date()

    evidences = EvidenceFile.objects.filter(expiry_date__lte=today)

    for e in evidences:
        Notification.objects.create(
            org_id=e.org_id,
            user_id=e.uploaded_by,
            type="RENEWAL_DUE",
            message="Renewal overdue",
            status="pending",
        )
      