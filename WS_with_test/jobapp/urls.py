from django.urls import path

import jobapp.views as jobapp

app_name = "jobapp"

urlpatterns = [
    path('', jobapp.JobTitleList.as_view(), name='index'),
    path('create/', jobapp.JobTitleCreate.as_view(), name='jobtitle_create'),
    path('update/<int:pk>/', jobapp.JobTitleUpdate.as_view(), name='jobtitle_update'),
    path('delete/<int:pk>/', jobapp.JobTitleDelete.as_view(), name='jobtitle_delete'),
]
