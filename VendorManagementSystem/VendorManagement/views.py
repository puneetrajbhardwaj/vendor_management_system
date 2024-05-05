# from django.shortcuts import render
from django.db.models import F , Sum
from .serializers import HistoricalPerformanceSerializer , PurchaseOrderSerializer , VendorSerializer
from .models import Vendor , PurchaseOrder ,HistoricalPerformance
from rest_framework import viewsets ,response
from rest_framework.decorators import action
from django.db.models.signals import pre_save , post_save
from django.dispatch import receiver 
from datetime import datetime


class VendorViewset(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @action(methods=['get'] , detail=True)
    def performance(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class PurchaseOrderViewset(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer



#Signals

@receiver(pre_save ,sender=PurchaseOrder)
def PurchaseOrderPreSave(sender,instance,**kwargs):
    if instance.pk:  # Check if the instance already exists (i.e., it's being updated)
        old_instance = PurchaseOrder.objects.get(pk=instance.pk)
        if old_instance.status != instance.status and instance.status == 'completed':
            PerformanceView(instance,old_instance)

def PerformanceView(instance,old_instance):
    vendor = instance.vendor
    date = datetime.now()
    queryset = PurchaseOrder.objects.filter(vendor=vendor).select_related('vendor').all()
    total_delivery_count = queryset.all().count()
    if instance.delivery_date <= old_instance.delivery_date:
        if vendor.on_time_delivery_rate:
            vendor.on_time_delivery_rate = ((vendor.on_time_delivery_rate)*100+1)/101
        else:
            on_time_delivery_rate = 1
    elif old_instance.delivery_date < instance.delivery_date:
        if vendor.on_time_delivery_rate:
            vendor.on_time_delivery_rate = ((vendor.on_time_delivery_rate)*100)/101
        else:
            on_time_delivery_rate = 0
    if instance.quality_rating:
        vendor.quality_rating_avg = (queryset.aggregate(rating_sum=Sum('quality_rating'))['rating_sum']+instance.quality_rating)/(total_delivery_count*5+5)
    if instance.quality_rating :
        vendor.average_response_time = (queryset.annotate(response_time=(F('acknowledgment_date')-F('issue_date'))).aggregate(total_response_time = Sum('response_time'))['total_response_time']+(instance.acknowledgment_date-instance.issue_date))/(total_delivery_count+1)
    vendor.save()



