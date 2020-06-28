from django.urls import path

import judapp.views as judapp

app_name = "judapp"

urlpatterns = [
    path('', judapp.JudSiteList.as_view(), name='index'),
    path('create/', judapp.JudSiteCreate.as_view(), name='judsite_create'),
    path('update/<int:pk>/', judapp.JudSiteUpdate.as_view(), name='judsite_update'),
    path('delete/<int:pk>/', judapp.JudSiteDelete.as_view(), name='judsite_delete'),
]
