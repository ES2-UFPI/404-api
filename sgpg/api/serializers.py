
from rest_framework import serializers
from .models import Cliente, Portal

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = '__all__'

class PortalSerializer(serializers.ModelSerializer):

    class Meta:

        model = Portal
        fields = '__all__'