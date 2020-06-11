from django.urls import path

import userapp.views as userapp

app_name = "userapp"

urlpatterns = [
    path('', userapp.WorkUserList.as_view(), name='index'),
    path('create/', userapp.WorkUserCreate.as_view(), name='workuser_create'),
    path('update/<int:pk>/', userapp.WorkUserUpdate.as_view(), name='workuser_update'),
    path('delete/<int:pk>/', userapp.WorkUserDelete.as_view(), name='workuser_delete'),
]
