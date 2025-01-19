from django.contrib import admin
from .models import DeviceInfo, Contact

class DeviceInfoAdmin(admin.ModelAdmin):
    list_display = ('user_agent', 'platform', 'ip', 'referrer', 'created_at')
    search_fields = ('user_agent', 'platform', 'language', 'ip', 'referrer')
    list_filter = ('platform', 'created_at')
    ordering = ('-created_at',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'subject', 'created_at')
    search_fields = ('name', 'email', 'mobile', 'subject')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

admin.site.register(DeviceInfo, DeviceInfoAdmin)
admin.site.register(Contact, ContactAdmin)