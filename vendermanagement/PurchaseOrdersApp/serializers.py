from rest_framework import serializers
from PurchaseOrdersApp import models

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PurchaseOrder
        fields = "__all__"