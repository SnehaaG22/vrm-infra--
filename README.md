# VRM Infrastructure Backend – MVP Automation

Production-grade MVP infrastructure for the VRM platform, integrating backend services, PostgreSQL, Redis, MinIO, and Celery with automated background jobs.

Features include evidence management with expiry tracking, renewal reminders, notifications API with org scoping, and end-to-end workflow validation.

Fully containerized and “one-command runnable” for development and testing.

# **Implemented Features:**

**_Backend & Infrastructure:_**

Django Backend

Celery Worker + Celery Beat (background automation)

Redis (message broker)

MinIO (object storage for evidence)

SQLite (local DB)

**Evidence Automation:**

Evidence Expiry Reminders

30 days before expiry

15 days before expiry

**Renewal Automation:**

Detects upcoming / overdue renewals

Marks status = OVERDUE

Creates notifications for admin/requester

**Notification System:**

APIs for list/read/mark-read with org scoping

Duplicate prevention using Notification.objects.get_or_create()

Retry safety with Celery autoretry (max_retries=3)

**MinIO Evidence Storage Strategy:**

Evidence files follow this structure:

org_id/vendor_id/assessment_id/question_id/file

Example: 1/10/101/5/document.pdf

# Local Setup Instructions:

1.Start Docker Services

docker-compose up -d --build

2.Run Migrations

docker exec -it vrm-backend-backend-1 bash

python manage.py makemigrations

python manage.py migrate

3.Seed Sample Evidence

docker exec -it vrm-backend-backend-1 bash

python manage.py shell

from apps.evidence.seeds import run

run()

exit()

4.Access Admin Panel

Django Admin: http://127.0.0.1:8000/admin/

Create superuser if needed:

python manage.py createsuperuser

5.MinIO Dashboard

http://localhost:9001

Username: minioadmin

Password: minioadmin

6.Testing Background Jobs & Notifications

**Manual Trigger**

docker compose exec backend python manage.py shell

from apps.evidence.tasks import evidence_expiry_reminder

from apps.renewals.tasks import renewal_due_reminder

**_#Run immediately (synchronous)_**

evidence_expiry_reminder()

renewal_due_reminder()

**_#Run async (Celery)_**

evidence_expiry_reminder.delay()

renewal_due_reminder.delay()

**Verify Notifications via API**

PowerShell example:

List notifications (for org 1):

iwr "http://localhost:8000/api/notifications/" -Headers @{ "org-id" = "1" } -UseBasicParsing

Mark a single notification as read (id=10):

iwr "http://localhost:8000/api/notifications/10/read/" -Method Patch -Headers @{ "org-id" = "1" } -UseBasicParsing

Mark all notifications as read:

iwr "http://localhost:8000/api/notifications/read-all/" -Method Post -Headers @{ "org-id" = "1" } -UseBasicParsing

7.Run Minimal Tests

docker compose exec backend python manage.py test

8. Run Automated Tests

docker compose exec backend python manage.py test apps.notifications

docker compose exec backend python manage.py test apps.evidence

9.Celery Logs

Worker:

docker-compose logs -f worker

Beat:

docker-compose logs -f beat

10.Trigger Reminder Jobs (Optional Manual Test):

Run Celery tasks manually to verify notifications:

docker compose exec backend python manage.py shell

from apps.evidence.tasks import evidence_expiry_reminders

from apps.renewals.tasks import renewal_due_reminders

#Trigger tasks

evidence_expiry_reminders()

renewal_due_reminders()

#List notifications

from apps.notifications.models import Notification

for n in Notification.objects.all():

print(n.id, n.org_id, n.user_id, n.type, n.status, n.message)

**_Services Included:_**

backend (Django)

worker (Celery)

beat (Celery scheduler)

redis

minio

**All services start via:**

docker-compose up -d

7 days before expiry

Creates notification records automatically for expiring evidence

# Verification Pack

Quick steps to confirm backend features are working after merges:

# Confirm MinIO Upload Path & Metadata Validation

**_Upload an evidence file via the API:_**

curl -X POST http://localhost:8000/api/evidence/upload/ \

-H "Content-Type: multipart/form-data" \

-F "file=@/full/path/to/your/file.pdf" \

-F "expiry_date=YYYY-MM-DD" \

-F "question_id=1"

**_Verify the uploaded path and metadata in MinIO:_**

mc alias set localminio http://localhost:9000 minioadmin minioadmin

mc ls localminio/your-bucket-name/path/to/evidence/

mc stat localminio/your-bucket-name/path/to/evidence/file.pdf

Confirm expiry_date and question_id are correctly stored in metadata.

# Confirm Celery Beat Schedules Fired

Check Celery Beat logs:

docker compose logs beat --tail=50

**_Check DB notifications created:_**

SELECT \* FROM notifications_notification ORDER BY created_at DESC LIMIT 5;

Ensure notifications respect org scoping.

# Confirm Duplicate Notification Prevention

Trigger the notification job twice.

Verify only one notification per event per user is created:

SELECT user_id, event_type, COUNT(\*) FROM notifications_notification

GROUP BY user_id, event_type

HAVING COUNT(\*) > 1;

Result should be empty if duplicates are prevented correctly.

# Automated Tests (CI / Local)

Minimal tests should run to verify critical behaviors:

Notification duplicate prevention

Reminder jobs create notifications with correct org scoping

Run tests:

docker compose exec backend python manage.py test apps.notifications

docker compose exec backend python manage.py test apps.evidence
