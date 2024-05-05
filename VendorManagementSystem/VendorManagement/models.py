from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=20)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20,unique=True)
    on_time_delivery_rate = models.FloatField(default=0) 
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)


class PurchaseOrder(models.Model): 
    po_number = models.CharField(max_length=20 ,unique=True)
    vendor = models.ForeignKey(Vendor , on_delete=models.CASCADE , related_name='purchase_order')
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(validators=[MaxValueValidator(5.0)],null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor , on_delete=models.CASCADE , related_name='historical_performance')
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

