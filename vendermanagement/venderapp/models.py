from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# from PurchaseOrdersApp import models

# Create your models here.
"""
Vendor Models to save vendor details
"""
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField(max_length=30)
    address = models.TextField()
    vendor_code = models.CharField(max_length=255,unique=True,editable=False)
    on_time_delivery_rate = models.FloatField(validators = [MinValueValidator(0),MaxValueValidator(100)],default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)
    is_active = models.BooleanField(default=0)
    is_archived = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_performance_metrics(self):
            completed_orders = self.purchaseorder_set.filter(status='completed')
            # On-Time Delivery Rate
            total_completed_orders = completed_orders.count()
            on_time_delivery_count = completed_orders.filter(delivery_date__lte=models.F('acknowledgment_date')).count()
            self.on_time_delivery_rate = (on_time_delivery_count / total_completed_orders) * 100 if total_completed_orders != 0 else 0

            # Quality Rating Average
            quality_ratings = completed_orders.exclude(quality_rating__isnull=True).values_list('quality_rating', flat=True)
            self.quality_rating_avg = sum(quality_ratings) / len(quality_ratings) if len(quality_ratings) != 0 else 0
            # Average Response Time
            response_times = completed_orders.exclude(acknowledgment_date__isnull=True).values_list('acknowledgment_date', 'issue_date')
            avg_response_time = sum([(ack_date - issue_date).total_seconds() for ack_date, issue_date in response_times]) / len(response_times) if len(response_times) != 0 else 0
            self.average_response_time = avg_response_time
            # Fulfilment Rate
            successful_fulfillments = completed_orders.filter(issue_date__isnull=False, acknowledgment_date__isnull=False)
            self.fulfillment_rate = (successful_fulfillments.count() / total_completed_orders) * 100 if total_completed_orders != 0 else 0

            print(self.on_time_delivery_rate)
            print(self.quality_rating_avg)
            print(self.average_response_time)
            print(self.fulfillment_rate,end="\n\n")
            self.save()