from rest_framework import serializers
from .models import DeviceInfo, Contact

class DeviceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInfo
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'