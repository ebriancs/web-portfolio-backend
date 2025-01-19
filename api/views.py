from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DeviceInfo, Contact
from .serializers import DeviceInfoSerializer, ContactSerializer
import logging

logger = logging.getLogger(__name__)

class DeviceInfoView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            mapped_data = {
                'user_agent': data.get('userAgent'),
                'platform': data.get('platform'),
                'language': data.get('language'),
                'ip': data.get('ip'),
                'referrer': data.get('referrer'),
            }
            logger.debug(f"mapped_data: {mapped_data}\n")
            serializer = DeviceInfoSerializer(data=mapped_data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Device info created successfully!'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request, *args, **kwargs):
        return Response({'message': 'Device info'}, status=status.HTTP_200_OK)
    

class ContactView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            mapped_data = {
                'name': data.get('name'),
                'email': data.get('email'),
                'mobile': data.get('mobile'),
                'subject': data.get('subject'),
                'message': data.get('message'),
            }
            logger.debug(f"mapped_data: {mapped_data}\n")
            logger.info(f"mapped_data: {mapped_data}\n")
            serializer = ContactSerializer(data=mapped_data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Message sent successfully!'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)