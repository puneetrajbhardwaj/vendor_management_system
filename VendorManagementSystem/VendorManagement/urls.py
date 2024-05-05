from django.urls import re_path,path
from VendorManagement import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers




urlpatterns = [
    
path('vendors/',views.VendorViewset.as_view({'get':'list' , 'post':'create'})),
path('vendors/<int:pk>/',views.VendorViewset.as_view({'get':'retrieve' , 'put':'update' ,'delete':'destroy'})),
path('purchase_orders/',views.PurchaseOrderViewset.as_view({'get':'list' , 'post':'create'})),
path('purchase_orders/<int:pk>/',views.PurchaseOrderViewset.as_view({'get':'retrieve' , 'put':'update' ,'delete':'destroy'})),
path('vendors/<int:pk>/performance/',views.VendorViewset.as_view({'get':'performance'})),
]



