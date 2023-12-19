from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
import json
from .classes import Vendor,HistoricalPerformance
from rest_framework.authtoken.models import Token


class VendorView(APIView):
    """
    Vendors Operations
    """
    def post(self,request,format="json"):
        try:
            vendor = Vendor(request)
            vendor_data = vendor.addVendor()
            data = {}
            data["statusCode"] = 200
            data["msg"] = "Vendor added succesfully"
            data['data'] = vendor_data
            return HttpResponse(json.dumps(data),content_type = 'application/json')
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while adding vendor"
            }
            return HttpResponse(json.dumps(data),content_type = 'application/json')
        
    def get(self,request,id=None,format="json"):
        try:
            if id:
                vendor = Vendor(request)
                vendor_data = vendor.getVendor(id)
                if vendor_data:
                    data = {
                        "StatusCode" : 200,
                        "msg"   : "Vendors data fetched succesfully",
                        "data"  : vendor_data
                    }
                else:
                    data = {
                        "StatusCode" : 200,
                        "msg"        : "Provide valid ID"
                    }
                return HttpResponse(json.dumps(data),content_type = 'application/json')

            if id is None:
                vendor = Vendor(request)
                count,vendor_list = vendor.listVendor()
                data = {
                    "StatusCode"    : 200,
                    "msg"           : "Vendors list fetched succesfully",
                    "count"         : count,
                    "data"          : vendor_list
                }
                return HttpResponse(json.dumps(data),content_type = 'application/json')
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while Fetching Vendor"
            }
            return HttpResponse(json.dumps(data),content_type = 'application/json')
        
    def put(self,request,id=None,format="json"):
        try:
            vendor = Vendor(request)
            vendor_data = vendor.updateVendor(id)
            return HttpResponse(json.dumps(vendor_data),content_type="application/json")
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while updating vendor"
            }
            return HttpResponse(json.dumps(data),content_type = 'application/json')
        
    def delete(self,request,id=None,format="json"):
        try:
            vendor = Vendor(request)
            vendor_data = vendor.deleteVendor(id)
            data = {
                "statusCode" : 200,
                "msg" : vendor_data
            }
            return HttpResponse(json.dumps(data),content_type="application/json")
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while Deleting Vendor"
            }
            return HttpResponse(json.dumps(data),content_type = 'application/json')

            
class HistoricalPerformanceView(APIView):
    """
    Historical performance calculations operations
    """

    def get(self,request,vendor_id=None,format="json"):
        try:
            historicalPerformance = HistoricalPerformance(request)
            historical_performance_data = historicalPerformance.getHistoricalPerformance(vendor_id)
            data = {}
            if historical_performance_data:
                data["statusCode"] = 200
                data["msg"] = "Vendor performance succesfully"
                data['data'] = historical_performance_data
                return HttpResponse(json.dumps(data),content_type = 'application/json')
            
            data["statusCode"] = 200
            data["msg"] = "Provide valid Vendor ID"
            return HttpResponse(json.dumps(data),content_type="application/json")
        except (AssertionError) as ex:
            data = {
                "statusCode" : 500,
                "msg" : "Something went wrong while fetching historical performance calculation"
            }
            return HttpResponse(json.dumps(data),content_type="application/json")
        
