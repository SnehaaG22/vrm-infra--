from django.test import TestCase
from .models import Notification

class NotificationTestCase(TestCase):
    def test_no_duplicate_notification(self):
        # Create first notification
        n1, created1 = Notification.objects.get_or_create(
            org_id=1, user_id=1, type="EVIDENCE_EXPIRY", message="Test Notification"
        )
        # Attempt duplicate
        n2, created2 = Notification.objects.get_or_create(
            org_id=1, user_id=1, type="EVIDENCE_EXPIRY", message="Test Notification"
        )
        # Should not create duplicate
        self.assertFalse(created2)
        self.assertEqual(Notification.objects.filter(org_id=1, user_id=1, type="EVIDENCE_EXPIRY").count(), 1)
