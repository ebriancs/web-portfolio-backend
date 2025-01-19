from django.db import models

from django.db import models

class DeviceInfo(models.Model):
    user_agent = models.TextField()
    platform = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    ip = models.GenericIPAddressField()
    referrer = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.platform} - {self.ip}"
