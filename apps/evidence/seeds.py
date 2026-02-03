from django.utils import timezone
from .models import EvidenceFile

def run():
    # ---------------- Sample Evidence Entry ----------------
    EvidenceFile.objects.create(
        org_id=1,
        assessment_id=101,
        question_id=5,
        file_url="http://minio/org1/vendor1/101/5/doc.pdf",
        uploaded_by=1,  # keep integer if your uploaded_by is IntegerField
        expiry_date=timezone.now().date(),
        file_type="pdf",
    )

    EvidenceFile.objects.create(
        org_id=2,
        assessment_id=102,
        question_id=8,
        file_url="http://minio/org2/vendor2/102/8/image.jpg",
        uploaded_by=2,
        expiry_date=timezone.now().date(),
        file_type="jpg",
    )

<<<<<<< HEAD
    print("Sample Evidence seeded successfully!")
=======
    print("Sample Evidence seeded successfully!")
>>>>>>> d271ac02bcff173701a74d6a74264cec6e1e213f
