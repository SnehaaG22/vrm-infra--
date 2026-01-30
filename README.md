# VRM Infrastructure Backend – MVP Automation

This repository contains the Infrastructure + Background Jobs + Evidence Storage automation for the VRM MVP.

***It implements:***

Django Backend

Celery Worker + Celery Beat (background automation)

Redis (message broker)

MinIO (object storage for evidence)

SQLite (local DB)

Evidence expiry reminders

Renewal due reminders

Notification system

***Features Implemented***

Evidence Automation

Evidence expiry reminders at:

30 days

15 days

7 days

Creates notification records automatically.

**Renewal Automation**

Detects overdue renewals

Marks status = OVERDUE

Creates notifications for admin/requester

**MinIO Evidence Storage Strategy**

All evidence files follow this structure:

org_id/vendor_id/assessment_id/question_id/file


Example:

1/10/101/5/document.pdf

# Local Setup Instructions

1️) Start Docker Services

From project root:

docker-compose up -d --build

2️) Run Migrations

docker exec -it vrm-backend-backend-1 bash

Inside container:

python manage.py makemigrations

python manage.py migrate

3️) Seed Sample Evidence

docker exec -it vrm-backend-backend-1 bash

python manage.py shell

from apps.evidence.seeds import run

run()

exit()

4) Access Admin Panel

http://127.0.0.1:8000/admin/

Create superuser if needed:

python manage.py createsuperuser

5) MinIO Dashboard
   
http://localhost:9001

Credentials:

Username: minioadmin

Password: minioadmin

6) Django Admin

http://localhost:8000/admin

7) Testing Background Jobs
   
Manual Trigger (for testing)

python manage.py shell

from apps.evidence.tasks import evidence_expiry_reminder

from apps.renewals.tasks import renewal_due_reminder

evidence_expiry_reminder()

renewal_due_reminder()

8) View Notifications

http://127.0.0.1:8000/admin/notifications/

9) Celery Logs

Worker:

docker-compose logs -f worker


Beat:

docker-compose logs -f beat

10) Services Included

backend (Django)

worker (Celery)

beat (Celery scheduler)

redis

minio

11) All started via:

docker-compose up -d





