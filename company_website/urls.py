"""
URL configuration for company_website project.
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path
from website import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files in both development and production
# Note: For production with many users, consider using cloud storage (AWS S3, Cloudinary, etc.)
if settings.DEBUG:
    # Development: use static() helper
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # Production: serve media files through Django
    urlpatterns += [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    ]
