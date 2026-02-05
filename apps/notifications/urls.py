from django.urls import path
from .views import NotificationListView, MarkReadView, MarkAllReadView

urlpatterns = [
    path("", NotificationListView.as_view(), name="notification-list"),
    path("<int:pk>/mark-read/", MarkReadView.as_view(), name="notification-mark-read"),
    path("read-all/", MarkAllReadView.as_view(), name="notification-mark-all-read"),
]
