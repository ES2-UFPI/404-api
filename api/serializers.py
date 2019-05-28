from rest_framework import serializers
from .models import Portal


class PortalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Portal
    fields = '__all__'
