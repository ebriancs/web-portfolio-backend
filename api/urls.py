from django.urls import path
from . import views

urlpatterns = [
    path('device-info/', views.DeviceInfoView.as_view(), name='DeviceInfo'),
    path('contact/', views.ContactView.as_view(), name='Contact'),
]
