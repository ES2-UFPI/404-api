from django.shortcuts import render
from rest_framework import generics
from .models import Portal
from .serializers import PortalSerializer


class PortalList(generics.ListCreateAPIView):

    queryset = Portal.objects.all()
    serializer_class = PortalSerializer


class PortalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portal.objects.all()
    serializer_class = PortalSerializer
