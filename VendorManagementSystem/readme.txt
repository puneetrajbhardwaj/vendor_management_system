Hi ,

I have developed the backend of the application you can set it up like a regular django application although I was confused with the points I am mentioning below.

1.average_response_time: FloatField - It should not be a float field as It stores Time.

2.Vendor Model and Historical Performance Model contains many simmilar fields and there is no seprate use mentioned for Historical Performance Model.

3.There is only one filed provided for delivery_date not Actual and Expected hence we cannot store or find which order was delayed.

4.Fulfilment Rate: Logic: Unable to develope this api as It is not mentioned what types of issues.


Endpoints Developed Successfully:

● POST /api/vendors/: Create a new vendor.
● GET /api/vendors/: List all vendors.
● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
● PUT /api/vendors/{vendor_id}/: Update a vendor's details.
● DELETE /api/vendors/{vendor_id}/: Delete a vendor.

● POST /api/purchase_orders/: Create a purchase order.
● GET /api/purchase_orders/: List all purchase orders with an option to filter by
vendor.
● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
● PUT /api/purchase_orders/{po_id}/: Update a purchase order.
● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

● GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance
metrics.

Backend logic Implimented Successfully:

Backend Logic for Performance Metrics
On-Time Delivery Rate:
● Calculated each time a PO status changes to 'completed'.
● Logic: Count the number of completed POs delivered on or before
delivery_date and divide by the total number of completed POs for that vendor.

Quality Rating Average:
● Updated upon the completion of each PO where a quality_rating is provided.
● Logic: Calculate the average of all quality_rating values for completed POs of
the vendor.
Average Response Time:
● Calculated each time a PO is acknowledged by the vendor.
● Logic: Compute the time difference between issue_date and
acknowledgment_date for each PO, and then find the average of these times
for all POs of the vendor.


Implimented all mentioned Models successfully.
Used Signals to impliment performance Submit.

Please Provide your feedback to My work 

Thanks
Puneet Bhardwaj



 