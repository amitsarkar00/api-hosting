from django.db import models
from django.conf import settings

# Create your models here.
class Resume(models.Model):
    document = models.FileField(upload_to='resume/', default=None, null=True)
    data = models.TextField(null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email