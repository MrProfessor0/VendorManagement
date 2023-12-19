from django.urls import path
from . import views

urlpatterns = [
    path('purchase_orders/',views.PurchaseOrderView.as_view()),
    path('purchase_orders/<int:id>/',views.PurchaseOrderView.as_view()),
    # post method
    path('purchase_orders/<int:po_id>/acknowledge/',views.AcknowledgePurchaseOrderView.as_view()),
]