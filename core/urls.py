
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('admin/', admin.site.urls), # URL pattern for the admin interface
	path('', include('predictor.urls'))# Include URLs from the 'predictor' app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 # Serve media files during development
