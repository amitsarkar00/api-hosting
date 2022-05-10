import math
import random
from django.conf import settings
from django.db import models
from users.models import User

def get_default_meeting_url():
    base_url = 'https://meet.jit.si/'
    digits = 16
    url = base_url + str(math.floor(random.random() * 10 ** digits))
    if Meeting.objects.filter(url=url).exists():
        return get_default_meeting_url()
    return url

class Meeting(models.Model):
    name = models.CharField(max_length=100, null=True)
    url = models.URLField(unique=True, default=get_default_meeting_url)
    hosted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='meeting_hosted_by',
        null=True,
        default=None
    )
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ended_at = models.DateTimeField(null=True, default=None)
    extra_fields = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name or self.url