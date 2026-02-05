from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
     # ... other paths
    path("api/notifications/", include("apps.notifications.urls")),
    path("api/evidence/", include("apps.evidence.urls")),


]
