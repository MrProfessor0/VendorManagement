from . import serializers
from . import models
from django.db.models import Q
from venderapp import models as venderappmodels


class PurchaseOrder:
    def __init__(self,request=None):
        if not request:
            raise AssertionError(f"Request Object is not provided")
        self.request = request

    def addPurchaseOrder(self):
        list = ['po_number','vendor','order_date', 'delivery_date','items','quantity']
        for paramas in list:
            if not self.request.data.get(paramas):
                raise AssertionError(f"Provide {paramas.replace('_',' ').title()} values")
        
        user = venderappmodels.Vendor.objects.filter(id=self.request.data.get('vendor'))
        if not user:
            raise AssertionError(f"provide valid vendor code")

        purchaseorder = models.PurchaseOrder.objects.create(
            po_number = self.request.data.get('po_number'),
            vendor = user[0],
            order_date = self.request.data.get('order_date'),
            delivery_date = self.request.data.get('delivery_date'),
            items = self.request.data.get('items'),
            quantity = self.request.data.get('quantity'),
            status = self.request.data.get('status',"pending")
        )
        purchase_order_serializer = serializers.PurchaseOrderSerializer(purchaseorder).data

        return purchase_order_serializer
    
    def getPurchaseOrder(self,id=None):
        if not id:
            raise AssertionError(f"Vendor Id is not provided")
        purchase_order = models.PurchaseOrder.objects.filter(id=id)

        if purchase_order:
            purchase_order_serializer = serializers.PurchaseOrderSerializer(purchase_order[0]).data
            return purchase_order_serializer
        
        return None

    def listPurchaseOrder(self):
        vendor_id = self.request.data.get("vendor_id",None)
        count = 0

        if vendor_id:
            purchase_order_list = models.PurchaseOrder.objects.filter(is_active=False,is_archived=False,vendor=vendor_id)
            vendors_serializer = serializers.PurchaseOrderSerializer(purchase_order_list,many=True).data
            return vendors_serializer
        else:
            is_active = self.request.data.get("is_active",False)
            is_archived = self.request.data.get("is_archived",False)
            offset = self.request.data.get("offset",0)
            limit = self.request.data.get("limit",10)

            count = models.PurchaseOrder.objects.filter(is_active=is_active,is_archived=is_archived).count()
            purchase_order_list = models.PurchaseOrder.objects.filter(is_active=is_active,is_archived=is_archived)[offset:offset+limit]
            vendors_serializer = serializers.PurchaseOrderSerializer(purchase_order_list,many=True).data
            return count,vendors_serializer
               
    def updatePurchaseOrder(self,id=None):
        if not id:
            raise AssertionError(f"VendorId is required to perform this action.")
        
        purchase_order = models.PurchaseOrder.objects.filter(id=id)

        if not purchase_order.exists():
            raise AssertionError(f"Invalid vendor id")

        purchase_order = purchase_order[0]        
        purchase_order_serializer = serializers.PurchaseOrderSerializer(purchase_order,data=self.request.data,partial=True)
        if purchase_order_serializer.is_valid():
            purchase_order_serializer.save()
            return purchase_order_serializer.data
        else:
            return purchase_order_serializer.errors
        
    def deletePurchaseOrder(self,id=None):
        if not id:
            raise AssertionError(f"VendorId is required to perform this action")
        
        purchase_order = models.PurchaseOrder.objects.filter(id=id)

        if not purchase_order.exists():
            raise AssertionError(f"Invalid vendor Id")
        purchase_order=purchase_order[0]        
        purchase_order_serializer = serializers.PurchaseOrderSerializer(purchase_order,data={"is_active":True,"is_archived":True},partial=True)
        
        if purchase_order_serializer.is_valid():
            purchase_order_serializer.save()
            return "Vendor deleted Succesfully"
        else:
            return purchase_order_serializer.errors

class PurchaseOrderUpdate():
    def __init__(self,request=None):
        if not request:
            raise AssertionError(f"Request Object is not provided")
        self.request = request

    def updatePurchaseOrder(self,po_id=None):

        if not self.request.data.get('acknowledgment_date'):
            raise AssertionError(f"Provide Acknowledgment Date")
        
        purchase_order = models.PurchaseOrder.objects.filter(id=po_id)
        
        if not purchase_order.exists():
            raise AssertionError(f"Invalid vendor id")
        
        purchase_order = purchase_order[0]        
        purchase_order_serializer = serializers.PurchaseOrderSerializer(purchase_order,data=self.request.data,partial=True)
        if purchase_order_serializer.is_valid():
            purchase_order_serializer.save()
            vendor = models.Vendor.objects.filter(id=purchase_order.vendor_id)
            vendor_data = vendor[0]
            vendor_data.update_performance_metrics()
            data = {
                "on_time_delivery_rate" : vendor_data.on_time_delivery_rate,
                "quality_rating_avg"    : vendor_data.quality_rating_avg,
                "average_response_time" : vendor_data.average_response_time,
                "fulfillment_rate"      : vendor_data.fulfillment_rate
            }
            print(data)
            return True
        else:
            return purchase_order_serializer.errors
