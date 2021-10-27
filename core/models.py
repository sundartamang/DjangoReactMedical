from django.db import models
from django.contrib.auth.models import Group,User
from django.utils import timezone
from django.conf import settings
from django.urls import reverse


# Create your models here.        
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    update_at  = models.DateTimeField(auto_now=True)
    is_active  = models.BooleanField(default=True, null=True, blank=True)
    
    class Meta:
        abstract = True
        
    def save(self, *args, **kwargs):
        self.update_at = timezone.now()
        return super().save(*args, **kwargs)
    
    def timestamp_pretty(self):
        return self.created_at.strftime('%b %e, %Y')
    

# Employee models
class Employee(TimeStamp):
    id           = models.AutoField(primary_key=True)
    name         = models.CharField(max_length=255)
    join_date    = models.DateField()
    phone        = models.CharField(max_length=255)
    address      = models.CharField(max_length=255)
    objects      = models.Manager()

class EmployeeSalary(TimeStamp):
    id            = models.AutoField(primary_key=True)
    employee_id   = models.ForeignKey(Employee,on_delete=models.CASCADE)
    salary_date   = models.DateField()
    salary_amount = models.CharField(max_length=255)
    objects       = models.Manager()

class EmployeeBank(TimeStamp):
    id              = models.AutoField(primary_key=True)
    bank_account_no = models.CharField(max_length=255)
    ifsc_no         = models.CharField(max_length=255)
    employee_id     = models.ForeignKey(Employee,on_delete=models.CASCADE)
    objects         = models.Manager()
    
    

# Customer models
class Customer(TimeStamp):
    id       = models.AutoField(primary_key=True)
    name     = models.CharField(max_length=255)
    address  = models.CharField(max_length=255)
    contact  = models.CharField(max_length=255)
    objects  = models.Manager()
    
class CustomerRequest(TimeStamp):
    id               = models.AutoField(primary_key=True)
    customer_name    = models.CharField(max_length=255)
    phone            = models.CharField(max_length=255)
    medicine_details = models.CharField(max_length=255)
    status           = models.BooleanField(default=False)
    prescription     = models.FileField(default="")
    objects          = models.Manager()
    


# Company models
class Company(TimeStamp):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=255)
    license_no  = models.CharField(max_length=255)
    address     = models.CharField(max_length=255)
    contact_no  = models.CharField(max_length=255)
    email       = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    objects     = models.Manager()

class CompanyAccount(TimeStamp):
    choices = ((1,"Debit"),(2,"Credit"))

    id               = models.AutoField(primary_key=True)
    company_id       = models.ForeignKey(Company,on_delete=models.CASCADE)
    transaction_type = models.CharField(choices=choices,max_length=255)
    transaction_amt  = models.CharField(max_length=255)
    transaction_date = models.DateField()
    payment_mode     = models.CharField(max_length=255)
    objects          = models.Manager()
    
class CompanyBank(TimeStamp):
    id              = models.AutoField(primary_key=True)
    bank_account_no = models.CharField(max_length=255)
    ifsc_no         = models.CharField(max_length=255)
    company_id      = models.ForeignKey(Company,on_delete=models.CASCADE)
    objects         = models.Manager()
    


# Medicine models
class Medicine(TimeStamp):
    id             = models.AutoField(primary_key=True)
    name           = models.CharField(max_length=255)
    medical_type   = models.CharField(max_length=255)
    buy_price      = models.CharField(max_length=255)
    sell_price     = models.CharField(max_length=255)
    c_gst          = models.CharField(max_length=255)
    s_gst          = models.CharField(max_length=255)
    batch_no       = models.CharField(max_length=255)
    shelf_no       = models.CharField(max_length=255)
    expire_date    = models.DateField()
    mfg_date       = models.DateField()
    company_id     = models.ForeignKey(Company, on_delete=models.CASCADE)
    description    = models.CharField(max_length=255)
    in_stock_total = models.IntegerField()
    qty_in_strip   = models.IntegerField()
    objects        = models.Manager()
    
class MedicineDetails(TimeStamp):
    id            = models.AutoField(primary_key=True)
    medicine_id   = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    salt_name     = models.CharField(max_length=255)
    salt_qty      = models.CharField(max_length=255)
    salt_qty_type = models.CharField(max_length=255)
    description   = models.CharField(max_length=255)
    objects       = models.Manager()
    
    

# Bills models
class Bill(TimeStamp):
    id          = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    objects     = models.Manager()
    

class BillDetails(TimeStamp):
    id          = models.AutoField(primary_key=True)
    bill_id     = models.ForeignKey(Bill,on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    qty         = models.IntegerField()
    objects     = models.Manager()
    
    
