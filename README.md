VRM Infrastructure Backend – MVP Automation
This repository contains the Infrastructure + Background Jobs + Evidence Storage automation for the VRM MVP.

Implemented Features:

Backend & Infrastructure:

Django Backend

Celery Worker + Celery Beat (background automation)

Redis (message broker)

MinIO (object storage for evidence)

SQLite (local DB)

Evidence Automation:

Evidence expiry reminders:

30 days before expiry

15 days before expiry

7 days before expiry

Creates notification records automatically for expiring evidence

Renewal Automation

Detects overdue renewals

Marks status = OVERDUE

Creates notifications for admin/requester

Notification System

Notification APIs (list/read/mark-read) with org scoping

Duplicate prevention using Notification.objects.get_or_create()

Retry safety with Celery autoretry (max_retries=3)

MinIO Evidence Storage Strategy

All evidence files follow this structure:

org_id/vendor_id/assessment_id/question_id/file

Example:

1/10/101/5/document.pdf

Local Setup Instructions
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

Access Admin Panel
http://127.0.0.1:8000/admin/

Create superuser if needed:

python manage.py createsuperuser

MinIO Dashboard
http://localhost:9001

Credentials:

Username: minioadmin

Password: minioadmin

Django Admin
http://localhost:8000/admin

Testing Background Jobs & Notifications:
Manual Trigger

python manage.py shell

from apps.evidence.tasks import evidence_expiry_reminder

from apps.renewals.tasks import renewal_due_reminder

evidence_expiry_reminder()

renewal_due_reminder()

Verify Notifications via API

#PowerShell

iwr "http://localhost:8000/api/notifications/?user_id=1&org_id=1" -UseBasicParsing

Run Minimal Tests:
docker compose exec backend python manage.py test

Celery Logs
Worker:

docker-compose logs -f worker

Beat:

docker-compose logs -f beat

Services Included
backend (Django)

worker (Celery)

beat (Celery scheduler)

redis

minio

All started via:
docker-compose up -d
