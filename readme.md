# Delivery Order in Django

```python
Status : in-progress
```

## Features

* Delivery Order Creation
* Delivery Quotation received from courier services
* Delivery Order allocation to Courier
* Collect from Warehouse
* Consignment Delivery - Driver will update and change status of Order.

### Model

* User ( Type :['User','Driver','Retailer','Consumer','warehouse'])
* Order
* Product
* Vehicle
* Rate - Courier rate

### Command for creation of Group and Permissions

* Model level Permission
* Object Level Permission
