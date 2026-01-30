from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

from apps.evidence.models import EvidenceFile


def run():

    User = get_user_model()
    user = User.objects.first()

    if not user:
        print("Create superuser first")
        return

    EvidenceFile.objects.create(
        org_id=1,
        assessment_id=1,
        question_id=1,
        file_url="dummy",
        uploaded_by=user,
        expiry_date=timezone.now().date() + timedelta(days=30),
        file_type="pdf"
    )

    print("Seed completed")
