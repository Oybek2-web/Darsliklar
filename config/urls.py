# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('fanlar.urls',namespace='fanlar')),
#         path('darsliklar', include('darsliklar.urls'))
#     ]
#
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# QUYIDAGI IMPORTNI QO'SHING:
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # LOGIN SAHIFASI UCHUN YO'L (Xatolik shu yerda tuzatiladi):
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('', include('fanlar.urls', namespace='fanlar')),
    path('darsliklar/', include('darsliklar.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)