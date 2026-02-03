from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
     # ... other paths
    path("api/notifications/", include("apps.notifications.urls")),
    path("api/evidence/", include("apps.evidence.urls")),

=======
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
>>>>>>> d271ac02bcff173701a74d6a74264cec6e1e213f
]
