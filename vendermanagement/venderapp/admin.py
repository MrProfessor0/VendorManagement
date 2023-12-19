from django.contrib import admin
from .models import Vendor

# Register your models here.

@admin.register(Vendor)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','contact_details','address','vendor_code', 'on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate','is_active','is_archived','created_at','updated_at']