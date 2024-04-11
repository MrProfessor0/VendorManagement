from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .classes import PurchaseOrder,PurchaseOrderUpdate
# from venderapp import models

# Create your views here.
class PurchaseOrderView(APIView):
    """
    Purchase Order Operations
    """
    def post(self,request,format="json"):
        try:
            purchaseorder = PurchaseOrder(request)
            vendor_data = purchaseorder.addPurchaseOrder()
            data = {
                "statusCode" : 200,
                "msg" : "Purchase Order added Suceesfully",
                "data" : vendor_data
            }
            return Response(json.dumps(data),content_type = 'application/json')
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while adding Purchase Order"
            }
            return Response(json.dumps(data),content_type = 'application/json')
        
    def get(self,request,id=None,format="json"):
        try:
            if id:
                purchaseorder = PurchaseOrder(request)
                purchase_order_data = purchaseorder.getPurchaseOrder(id)
                if purchase_order_data:
                    data = {
                        "statusCode" : 200,
                        "msg" : "Purchase Orders data fethced succesfully",
                        "data" : purchase_order_data
                    }
                    return Response(json.dumps(purchase_order_data),content_type = 'application/json')
                
                data = {
                    "statusCode" : 200,
                    "msg" : "Purchase Orders data Not Found",
                }
                return Response(json.dumps(data),content_type = 'application/json')

            if id is None:
                purchaseorder = PurchaseOrder(request)
                count,purchase_order_list = purchaseorder.listPurchaseOrder()
                data = {
                    "statusCode" : 200,
                    "msg" : "Purchase Orders list fethced succesfully",
                    "count" : count,
                    "data" : purchase_order_list
                }
                return Response(json.dumps(data),content_type = 'application/json')
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while adding vendor"
            }
            return Response(json.dumps(data),content_type = 'application/json')
        
    def put(self,request,id=None,format="json"):
        try:
            purchaseorder = PurchaseOrder(request)
            purchase_order_data = purchaseorder.updatePurchaseOrder(id)
            data = {
                "statusCode" : 200,
                "msg" : "Purchase order updated succesfully"
            }
            return Response(json.dumps(data),content_type="application/json")
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while adding vendor"
            }
            return Response(json.dumps(data),content_type = 'application/json')
        
    def delete(self,request,id=None,format="json"):
        try:
            purchaseorder = PurchaseOrder(request)
            purchase_order_data = purchaseorder.deletePurchaseOrder(id)
            data = {
                "statusCode" : 200,
                "msg" : "Purchase order deleted succesfully"
            }
            return Response(json.dumps(data),content_type="application/json")
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while adding vendor"
            }
            return Response(json.dumps(data),content_type = 'application/json')
        

class AcknowledgePurchaseOrderView(APIView):
    """
    for Acknowledge update
    """
    def post(self,request,po_id=None,format="json"):
        try:
            purchase_order_update = PurchaseOrderUpdate(request)
            data = purchase_order_update.updatePurchaseOrder(po_id)
            # if data:
            print(data)
            data = {
                "statusCode" : 200,
                "msg" : "Successfully updated the status"
            }
            # models.Vendor.update_performance_metrics(self)
            return Response(json.dumps(data),content_type='application/json')
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while updating acknowldge update"
            }
            return Response(json.dumps(data),content_type = 'application/json')