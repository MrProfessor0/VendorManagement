from . import serializers
from . import models

class Vendor:
    """
    Vendor classess to perform CRUD operation
    """
    def __init__(self,request=None):
        if not request:
            raise AssertionError(f"Request Object is not provided")
        self.request = request

    def addVendor(self):
        list = ['name','contact_details','address','vendor_code']
        for params in list:
            if not self.request.data.get(params):
                raise AssertionError(f"Please provide {params.replace('_',' ').title()}")
            
        vendor = models.Vendor.objects.create(
            name = self.request.data.get('name'),
            contact_details = self.request.data.get('contact_details'),
            address = self.request.data.get('address'),
            vendor_code = self.request.data.get('vendor_code')
        )
        vendor.update_performance_metrics()
        vendor_serializer = serializers.VendorSerializer(vendor).data
        return vendor_serializer
    
    def getVendor(self,id=None):
        if not id:
            raise AssertionError(f"Vendor Id is not provided")

        vendor = models.Vendor.objects.filter(id=id)

        if vendor:
            vendors_serializer = serializers.VendorSerializer(vendor[0]).data
            return vendors_serializer
        
        return None

    def listVendor(self):
        is_active = self.request.data.get("is_active",False)
        is_archived = self.request.data.get("is_archived",False)
        offset = self.request.data.get("offset",0)
        limit = self.request.data.get("limit",10)

        count = models.Vendor.objects.filter(is_active=is_active,is_archived=is_archived).count()

        vendors = models.Vendor.objects.filter(is_active=is_active,is_archived=is_archived)[offset:offset+limit]
        vendors_serializer = serializers.VendorSerializer(vendors,many=True).data
        return count,vendors_serializer
    
    def updateVendor(self,id=None):
        if not id:
            raise AssertionError(f"VendorId is required to perform this action.")
        
        vendor = models.Vendor.objects.filter(id=id)

        if not vendor.exists():
            raise AssertionError(f"Invalid vendor id")

        vendor = vendor[0]
        vendor.update_performance_metrics()
        vendor_serializer = serializers.VendorSerializer(vendor,data=self.request.data,partial=True)
        if vendor_serializer.is_valid():
            vendor_serializer.save()
            return vendor_serializer.data
        else:
            return vendor_serializer.errors
       
    def deleteVendor(self,id=None):
        if not id:
            raise AssertionError(f"VendorId is required to perform this action")
        
        vendor = models.Vendor.objects.filter(id=id)

        if not vendor.exists():
            raise AssertionError(f"Invalid vendor Id")
        vendor=vendor[0]        
        vendor_serializer = serializers.VendorSerializer(vendor,data={"is_active":True,"is_archived":True},partial=True)
        
        if vendor_serializer.is_valid():
            vendor_serializer.save()
            return "Vendor deleted Succesfully"
        else:
            return vendor_serializer.errors

class HistoricalPerformance:
    def __init__(self,request=None):
        if not request:
            raise AssertionError(f"Request Object is not provided")
        self.request = request
    
    def getHistoricalPerformance(self,vendor_id=None):
        if not vendor_id:
            raise AssertionError(f"Vendor Id is not provided")

        offset = self.request.data.get("offset",0)
        limit = self.request.data.get("limit",10)

        vendor_data = models.Vendor.objects.filter(id=vendor_id)[offset:offset+limit]
        if vendor_data:
            vendor_data = vendor_data[0]
            data = {
                "on_time_delivery_rate" : vendor_data.on_time_delivery_rate,
                "quality_rating_avg"    : vendor_data.quality_rating_avg,
                "average_response_time" : vendor_data.average_response_time,
                "fulfillment_rate"      : vendor_data.fulfillment_rate
            }
            print(data)
            return data
        
        return False
