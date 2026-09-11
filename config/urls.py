from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('residentes/', include('residentes.urls')),
    path('pagos/', include('pagos.urls')),
    path('accesos/', include('accesos.urls')),
    path('servicios/', include('servicios.urls')),
    path('avisos/', include('notificaciones.urls')),
    path('', include('dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
