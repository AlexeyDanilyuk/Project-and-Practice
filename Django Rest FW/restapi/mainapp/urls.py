from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('add_account/', mainapp.AccountCreate.as_view(), name='get_post_account'),
]
