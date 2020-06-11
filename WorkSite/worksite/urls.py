from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='main')),
    path('judsites/', include('judapp.urls', namespace='judapp')),
    path('jobtitles/', include('jobapp.urls', namespace='jobapp')),
    path('workusers/', include('userapp.urls', namespace='userapp')),
    path('items/', include('itemsapp.urls', namespace='itemsapp')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('auth/verify/', include("social_django.urls", namespace="social")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
