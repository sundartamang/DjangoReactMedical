from django.contrib import admin
from core.models import (
    Employee,
    EmployeeSalary,
    EmployeeBank,
    Customer,
    CustomerRequest,
    Company,
    CompanyAccount,
    CompanyBank,
    Medicine,
    MedicineDetails,
    Bill,
    BillDetails
)

# Register your models here.
admin.site.register(Employee)
admin.site.register(EmployeeSalary)
admin.site.register(EmployeeBank)
admin.site.register(Customer)
admin.site.register(CustomerRequest)
admin.site.register(Company)
admin.site.register(CompanyAccount)
admin.site.register(CompanyBank)
admin.site.register(Medicine)
admin.site.register(MedicineDetails)
admin.site.register(Bill)
admin.site.register(BillDetails)