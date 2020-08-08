from django.shortcuts import render

from rest_framework import viewsets
from .models import Certificate
from .serializers import CertificateModelSerializer
# Create your views here.

class CertificateModelViewSetView(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateModelSerializer
