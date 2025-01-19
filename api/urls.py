from django.urls import path
from . import views

urlpatterns = [
    path('device-info/', views.DeviceInfoView.as_view(), name='DeviceInfo'),
]
