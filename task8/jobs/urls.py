from django.urls import path
from .views import (
    JobListView,
    JobCreateView,
    ApplicationCreateView,
    CompanyApplicationListView,
)

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),

    path('post-job/', JobCreateView.as_view(), name='job_create'),

    path('apply/<int:job_id>/', ApplicationCreateView.as_view(), name='apply_job'),

    path('company/applications/', CompanyApplicationListView.as_view(), name='company_applications'),
]