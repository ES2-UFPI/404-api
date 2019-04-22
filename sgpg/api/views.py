from django.shortcuts import render
from rest_framework import generics
from .models import Cliente, Portal
from .serializers import ClienteSerializer, PortalSerializer

class ClienteList(generics.ListCreateAPIView):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class PortalList(generics.ListCreateAPIView):

    queryset = Portal.objects.all()
    serializer_class = PortalSerializer


class PortalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portal.objects.all()
    serializer_class = PortalSerializer