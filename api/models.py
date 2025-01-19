from django.db import models

from django.db import models

class DeviceInfo(models.Model):
    user_agent = models.TextField(blank=True, null=True)
    platform = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    referrer = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.platform} - {self.ip}"

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name