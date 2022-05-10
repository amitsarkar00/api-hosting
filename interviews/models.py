from django.db import models
from django.conf import settings
from jobs.models import Job


class Interview(models.Model):
    title = models.CharField(max_length=100, null=True)
    candidate = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='interview_candidate',
        null=True
    )
    hr = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='interview_hr',
        null=True
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.SET_NULL,
        null=True
    )
    verified_by_candidate = models.BooleanField(default=False)
    verified_by_hr = models.BooleanField(default=False)
    scheduled_datetime = models.DateTimeField(null=True)
    round1 = models.BooleanField(null=True, default=None)
    round2 = models.BooleanField(null=True, default=None)
    round3 = models.BooleanField(null=True, default=None)
    feedback = models.TextField(null=True, blank=True)
    selected = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    extra_fields = models.TextField(null=True, blank=True)
