import { PrismaClient, Role } from "@prisma/client";

const prisma = new PrismaClient();

async function main() {
  const org = await prisma.org.create({
    data: {
      name: "MIT Test Org",
      users: {
        create: [
          { email: "admin@mit.com", password: "admin123", role: Role.ADMIN },
          {
            email: "reviewer@mit.com",
            password: "review123",
            role: Role.REVIEWER,
          },
          {
            email: "requester@mit.com",
            password: "request123",
            role: Role.REQUESTER,
          },
        ],
      },
    },
  });

  const vendor = await prisma.vendor.create({
    data: {
      name: "Vendor A",
      orgId: org.id,
      users: {
        create: [
          { email: "vendor1@vendor.com" },
          { email: "vendor2@vendor.com" },
        ],
      },
    },
  });

  const template = await prisma.template.create({
    data: {
      name: "Security Assessment",
      versions: {
        create: [
          {
            version: 1,
            sections: {
              create: [
                {
                  name: "Authentication",
                  questions: {
                    create: [
                      { text: "Does the vendor support MFA?", weight: 1 },
                      { text: "Password policy compliance?", weight: 1 },
                    ],
                  },
                },
              ],
            },
          },
        ],
      },
    },
  });

  console.log("Seed completed");
}

main()
  .catch((e) => console.error(e))
  .finally(async () => {
    await prisma.$disconnect();
  });
