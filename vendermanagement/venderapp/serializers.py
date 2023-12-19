from rest_framework import serializers
from venderapp import models

# Serializer for Vendor data
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = "__all__"