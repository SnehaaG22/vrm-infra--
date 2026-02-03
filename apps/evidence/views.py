from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EvidenceFile
import datetime

class EvidenceUploadView(APIView):
    def post(self, request):
        data = request.data
        # Validate required metadata
        expiry_date = data.get("expiry_date")
        question_id = data.get("question_id")
        assessment_id = data.get("assessment_id")
        org_id = data.get("org_id")
        uploaded_by = data.get("uploaded_by")
        file_url = data.get("file_url")
        file_type = data.get("file_type")

        if not expiry_date or not question_id:
            return Response({"error": "expiry_date and question_id required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            expiry_date = datetime.datetime.strptime(expiry_date, "%Y-%m-%d").date()
            if expiry_date < datetime.date.today():
                return Response({"error": "expiry_date cannot be in the past"}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({"error": "Invalid expiry_date format. Use YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)

        # MinIO path convention: <org_id>/<assessment_id>/<question_id>/<filename>
        evidence = EvidenceFile.objects.create(
            org_id=org_id,
            assessment_id=assessment_id,
            question_id=question_id,
            file_url=file_url,
            uploaded_by=uploaded_by,
            expiry_date=expiry_date,
            file_type=file_type,
        )
        return Response({"detail": "Evidence uploaded", "id": evidence.id}, status=status.HTTP_201_CREATED)
