# VRM / TPRM Backend Setup

This is the backend for the Vendor Risk Management (VRM) / Third Party Risk Management (TPRM) system. It uses **Node.js**, **Express**, **Prisma**, and **PostgreSQL**.

## 1️. Prerequisites

- Docker & Docker Compose
- Node.js (v18+ recommended)
- npm

## 2.Start Database

```bash
docker-compose up -d

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
