from django.db import models


# Create your models here.
class UserLogin(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)


class spare_part(models.Model):
    spare_part_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    quantity_available = models.CharField(max_length=200)
    supplier_id = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    photo = models.FileField(upload_to='documents/')


class supplier(models.Model):
    sid = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    spare_part_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)


class customer(models.Model):
    cid = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=200)



class order(models.Model):
    ord_id = models.CharField(max_length=20)
    date = models.CharField(max_length=50)
    status = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    spare_part_id = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)


class payment(models.Model):
    pid = models.CharField(max_length=20)
    ord_id = models.CharField(max_length=50)
    date = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)


class shipping(models.Model):
    sid = models.CharField(max_length=20)
    ord_id = models.CharField(max_length=50)
    shipping_date = models.CharField(max_length=200)
    estimated_delivery_date = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)


from django.db import models

# Create your models here.
