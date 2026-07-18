from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fanlar.urls', namespace='fanlar')),
    path('darsliklar/', include('darsliklar.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('tolov/', include('tolov.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)