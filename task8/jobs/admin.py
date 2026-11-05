from django.contrib import admin
from django.db.models import Count

from .models import Job, Application


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'company',
        'location',
        'job_type',
        'application_count',
        'created_at',
    )

    list_filter = ('job_type', 'location')

    search_fields = ('title', 'company__username')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        return queryset.annotate(
            total_applications=Count('applications')
        )

    @admin.display(description='Applications', ordering='total_applications')
    def application_count(self, obj):
        return obj.total_applications


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'job',
        'applicant',
        'applied_at',
    )

    list_filter = ('applied_at',)

    search_fields = (
        'job__title',
        'applicant__username',
    )