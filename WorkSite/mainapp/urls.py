from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.ArmList.as_view(), name='arm_list'),
    path('create/', mainapp.ArmCreate.as_view(), name='create'),
    path('delete/<int:pk>/', mainapp.ArmDelete.as_view(), name='delete'),
    path('update/<int:pk>/', mainapp.ArmUpdate.as_view(), name='update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
