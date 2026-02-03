# MinIO Path Strategy

Evidence Storage Path:

org_id/vendor_id/assessment_id/question_id/filename

Example:
1/22/101/5/policy.pdf

# How to Test Tasks Locally

1. Open Django shell:

   ```bash
   python manage.py shell
   ```

2. Run Renewal Due Reminder Task:

   ```python
   from apps.renewals.tasks import renewal_due_reminder
   renewal_due_reminder()
   ```

3. Run Evidence Expiry Reminder Task:

   ```python
   from apps.evidence.tasks import evidence_expiry_reminder
   evidence_expiry_reminder()
   ```

4. Check notifications in the database:

   ```python
   from apps.notifications.models import Notification
   Notification.objects.all()
   ```
