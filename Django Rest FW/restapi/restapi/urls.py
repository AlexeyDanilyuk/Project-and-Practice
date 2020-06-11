from django.contrib import admin
from django.urls import path, include

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
