from django.contrib import admin
from .models import DeviceInfo

class DeviceInfoAdmin(admin.ModelAdmin):
    list_display = ('user_agent', 'platform', 'language', 'ip', 'created_at')
    search_fields = ('user_agent', 'platform', 'language', 'ip')
    list_filter = ('platform', 'language', 'created_at')
    ordering = ('-created_at',)

admin.site.register(DeviceInfo, DeviceInfoAdmin)