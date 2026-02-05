from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification
from apps.notifications.serializers import NotificationSerializer


# List notifications for an org (org-id passed in headers)
class NotificationListView(ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        org_id = self.request.headers.get("org-id")
        return Notification.objects.filter(
            org_id=org_id
        ).order_by("-created_at")

# Mark a single notification as read
class MarkReadView(UpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def patch(self, request, *args, **kwargs):
        notif = self.get_object()
        notif.status = "read"
        notif.save()
        return Response({"status": "ok"})

# Mark all notifications as read for the org
class MarkAllReadView(APIView):
    def post(self, request):
        org_id = request.headers.get("org-id")
        Notification.objects.filter(
            org_id=org_id,
            status="unread"
        ).update(status="read")
        return Response({"status": "ok"})