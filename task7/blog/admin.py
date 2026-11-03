from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'author',
        'published_date',
        'status'
    )

    search_fields = (
        'title',
        'body',
        'author__username'
    )

    list_filter = (
        'status',
        'published_date'
    )

    ordering = ('-published_date',)

    list_per_page = 10