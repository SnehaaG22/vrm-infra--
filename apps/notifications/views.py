from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Notification

class NotificationListView(APIView):
    def get(self, request):
        user_id = request.query_params.get("user_id")
        org_id = request.query_params.get("org_id")
        notifications = Notification.objects.filter(user_id=user_id, org_id=org_id)
        data = [
            {
                "id": n.id,
                "type": n.type,
                "message": n.message,
                "status": n.status,
                "created_at": n.created_at,
            } for n in notifications
        ]
        return Response(data, status=status.HTTP_200_OK)


class NotificationDetailView(APIView):
    def get(self, request, pk):
        try:
            n = Notification.objects.get(pk=pk)
        except Notification.DoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({
            "id": n.id,
            "type": n.type,
            "message": n.message,
            "status": n.status,
            "created_at": n.created_at,
        }, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Mark as read"""
        try:
            n = Notification.objects.get(pk=pk)
        except Notification.DoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        n.status = "read"
        n.save()
        return Response({"detail": "Marked as read"}, status=status.HTTP_200_OK)
