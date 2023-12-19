from django.contrib import admin
from .models import PurchaseOrder

# Register your models here.

@admin.register(PurchaseOrder)
class PurchaseOrder(admin.ModelAdmin):
    list_display = ['id','po_number','vendor','order_date','delivery_date','items','quantity','status','quality_rating','issue_date','acknowledgment_date','is_active','is_archived','created_at','updated_at']

