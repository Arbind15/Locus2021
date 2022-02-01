from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path("", include('covid_detection.urls')),
                  path('authentication/', include('authentication.urls')),
                  path('scheduler/', include('scheduler.urls')),
                  path('messaging/', include('messenger.urls')),
                  path('hos/', include('hospital_manager.urls')),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
