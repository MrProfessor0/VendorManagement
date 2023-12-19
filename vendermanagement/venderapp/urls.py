from django.urls import path
from . import views

urlpatterns = [
    path('vendors/',views.VendorView.as_view()),
    path('vendors/<int:id>/',views.VendorView.as_view()),
    path('vendors/<int:vendor_id>/performance/',views.HistoricalPerformanceView.as_view()),
]