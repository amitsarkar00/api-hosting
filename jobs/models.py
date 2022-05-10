from django.db import models
from django.conf import settings

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True, blank=True)
    positions = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    min_qualification = models.TextField(null=True, blank=True)
    min_experience = models.IntegerField(null=True)
    required_skills = models.TextField(null=True, blank=True)
    ctc = models.FloatField(null=True)
    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    publish_date = models.DateField(auto_now_add=True)
    extra_fields = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title