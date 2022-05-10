from django.db import models
from django.conf import settings

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=50, null=True)
    file = models.FileField(upload_to='docs/', default=None, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    extra_fields = models.TextField(null=True)

    def __str__(self):
        return self.user.email