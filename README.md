<<<<<<< HEAD
<<<<<<< HEAD
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
=======
#VRM / TPRM Backend Setup

This is the backend for the Vendor Risk Management (VRM) / Third Party Risk Management (TPRM) system. It uses **Node.js**, **Express**, **Prisma**, and **PostgreSQL**.

##1️. Prerequisites
-Docker & Docker Compose
-Node.js (v18+ recommended)
-npm

##2.Start Database

```bash
docker-compose up-d

Starts PostgreSQL and pgAdmin.
Wait a few seconds for the database to initialize.
Access pgAdmin at http://localhost:5050
 with:
Email: admin@admin.com
Password: admin

## 3️.Install Dependencies
npm install
Installs all Node.js dependencies including Prisma, Express, and TypeScript.

## 4️.Run Migrations
npm run migrate
Applies the Prisma schema to the PostgreSQL database.
Creates tables and relationships.

## 5️.Seed Database
npm run seed
Populates the database with sample data, including organizations, users, vendors, and templates.

## 6️.Start Backend Server
npm run dev
Runs the Express server on http://localhost:3000
You should see:
Server running on http://localhost:3000

## 7️.Test Users
Email	Password	Role
admin@demo.com
	password	ADMIN
reviewer@demo.com
	password	REVIEWER
vendor@crm.com
	password	VENDOR

    ## 9️.Notes
Ensure your backend .env file is correctly configured:
DATABASE_URL=postgresql://vrm:vrm@localhost:5432/vrm_db
If Prisma complains about missing relations, double-check the schema.prisma file for two-way relations.
Use npx prisma generate if you make changes to the schema.

## 10.Useful Commands
# Format Prisma schema
npx prisma format
# Generate Prisma client
npx prisma generate
# Open Prisma studio (DB GUI)
npx prisma studio
# Stop database containers
docker-compose down

```
>>>>>>> ab7bb2a0b8db3d3324069e97d3cf8a9d8be898a7
=======
# VRM Infrastructure Backend – MVP Automation

This repository contains the Infrastructure + Background Jobs + Evidence Storage automation for the VRM MVP.

***Implemented Features:***

**Backend & Infrastructure:**

Django Backend

Celery Worker + Celery Beat (background automation)

Redis (message broker)

MinIO (object storage for evidence)

SQLite (local DB)

**Evidence Automation:**

Evidence expiry reminders:

30 days before expiry

15 days before expiry

7 days before expiry

Creates notification records automatically for expiring evidence

**Renewal Automation**

Detects overdue renewals

Marks status = OVERDUE

Creates notifications for admin/requester

**Notification System**

Notification APIs (list/read/mark-read) with org scoping

Duplicate prevention using Notification.objects.get_or_create()

Retry safety with Celery autoretry (max_retries=3)

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

7) Testing Background Jobs & Notifications:
   
  **Manual Trigger**
  
 python manage.py shell
 
from apps.evidence.tasks import evidence_expiry_reminder

from apps.renewals.tasks import renewal_due_reminder

evidence_expiry_reminder()

renewal_due_reminder()

**Verify Notifications via API**

#PowerShell

iwr "http://localhost:8000/api/notifications/?user_id=1&org_id=1" -UseBasicParsing

8) Run Minimal Tests:

docker compose exec backend python manage.py test


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







>>>>>>> d271ac02bcff173701a74d6a74264cec6e1e213f
