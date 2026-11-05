from django.db import models
from django.contrib.auth.models import User


class InternProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='intern_profile'
    )

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=100)
    skills = models.TextField(blank=True)
    bio = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name