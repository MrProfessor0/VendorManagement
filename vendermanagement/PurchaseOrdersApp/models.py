from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class PurchaseOrder(models.Model):
    status_choices = [
        ("pending","Pending"),
        ("completed","Completed"),
        ("canceled","Canceled")
    ]
    po_number = models.CharField(max_length=255,unique=True)
    vendor = models.ForeignKey('venderapp.Vendor',on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField(validators = [MinValueValidator(0)])
    status = models.CharField(max_length=255,choices=status_choices,default="pending")
    quality_rating = models.FloatField(validators = [MinValueValidator(0),MaxValueValidator(5)],default=0)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True,default=None)
    is_active = models.BooleanField(default=0)
    is_archived = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

@receiver(post_save,sender=PurchaseOrder)
def update_vendor_performance_metrics(sender,instance,**kwargs):
    instance.vendor.update_performance_metrics()