from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DeviceInfo
from .serializers import DeviceInfoSerializer

class DeviceInfoView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            print(data, sep='\n')
            mapped_data = {
                'user_agent': data.get('userAgent'),
                'platform': data.get('platform'),
                'language': data.get('language'),
                'ip': data.get('ip'),
                'referrer': data.get('referrer'),
            }
            print(mapped_data, sep='\n')
            serializer = DeviceInfoSerializer(data=mapped_data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Device info created successfully!'}, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request, *args, **kwargs):
        return Response({'message': 'Device info'}, status=status.HTTP_200_OK)
    