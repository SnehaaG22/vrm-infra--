from django.test import TestCase
from apps.evidence.models import EvidenceFile
from django.utils import timezone
import datetime

class EvidenceTestCase(TestCase):
    def test_metadata_validation(self):
        future_date = (timezone.now() + datetime.timedelta(days=5)).date()
        evidence = EvidenceFile.objects.create(
            org_id=1,
            assessment_id=101,
            question_id=5,
            file_url="http://minio/org1/101/5/doc.pdf",
            uploaded_by=1,
            expiry_date=future_date,
            file_type="pdf",
        )
        self.assertEqual(evidence.expiry_date, future_date)
        self.assertEqual(evidence.question_id, 5)
