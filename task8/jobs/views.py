from django.views.generic import (
    ListView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Job, Application
from .forms import JobForm, ApplicationForm


class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    ordering = ['-created_at']

class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job_list')

    def form_valid(self, form):
        form.instance.company = self.request.user

        messages.success(self.request, "Job posted successfully!")

        return super().form_valid(form)
class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'jobs/application_form.html'
    success_url = reverse_lazy('job_list')

    def dispatch(self, request, *args, **kwargs):
        self.job = get_object_or_404(
            Job,
            pk=kwargs['job_id']
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if Application.objects.filter(
            job=self.job,
            applicant=self.request.user
        ).exists():

            form.add_error(
                None,
                "You have already applied for this job."
            )
            return self.form_invalid(form)

        form.instance.job = self.job
        form.instance.applicant = self.request.user

        messages.success(self.request, "Application submitted!")

        return super().form_valid(form)


class CompanyApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'jobs/application_list.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(
            job__company=self.request.user
        ).select_related('job', 'applicant').order_by('-applied_at')