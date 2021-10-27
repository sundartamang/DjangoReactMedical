from rest_framework import serializers
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

# Employee serializers
class EmployeeSerliazer(serializers.ModelSerializer):
    class Meta:
        model  = Employee
        fields = "__all__"
        
class EmployeeSalarySerliazer(serializers.ModelSerializer):
    class Meta:
        model  = EmployeeSalary
        fields = "__all__"
        
    # To access foreign key data we override method here
    # beacue we have employee_id in EmployeeSalary model
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['employee'] = EmployeeSerliazer(instance.employee_id).data
        return response
    
class EmployeeBankSerliazer(serializers.ModelSerializer):
    class Meta:
        model  = EmployeeBank
        fields = "__all__"
        
    # To access foreign key data we override method here
    # beacue we have employee_id in EmployeeBank model
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['employee'] = EmployeeSerliazer(instance.employee_id).data
        return response




# Customer serializers
class CustomerSerliazer(serializers.ModelSerializer):
    class Meta:
        model  = Customer
        fields = "__all__"
        
class CustomerRequestSerliazer(serializers.ModelSerializer):
    class Meta:
        model  = CustomerRequest
        fields = "__all__"



# Company serializers
class CompanySerliazer(serializers.ModelSerializer):
    class Meta:
        model  = Company
        fields = "__all__"

class CompanyBankSerliazer(serializers.ModelSerializer):
    class Meta:
        model  = CompanyBank
        fields = "__all__"
    
    # To access foreign key data we override method here
    # beacue we have company_id in CompanyBank model
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerliazer(instance.company_id).data
        return response
    
class CompanyAccountSerliazer(serializers.ModelSerializer):
    class Meta:
        model  = CompanyAccount
        fields = "__all__"
    
    # To access foreign key data we override method here
    # beacue we have company_id in CompanyBank model
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerliazer(instance.company_id).data
        return response
    
    


# Medicine serializers
class MedicineSerliazer(serializers.ModelSerializer):
    class Meta:
        model  = Medicine
        fields = "__all__"
    
    # To access foreign key data we override method here
    # beacue we have company_id in Medicine model
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerliazer(instance.company_id).data
        return response
    
class MedicineDetailsSerliazer(serializers.ModelSerializer):
    class Meta:
        model  = MedicineDetails
        fields = "__all__"
    
    # To access foreign key data we override method here
    # beacue we have medicine_id in MedicalDetails model
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['medicine'] = MedicineSerliazer(instance.medicine_id).data
        return response
    


# Bill serializers
class BillSerliazer(serializers.ModelSerializer):
    class Meta:
        model  = Bill
        fields = "__all__"
        
    # To access foreign key data we override method here
    # beacue we have company_id in Bill model
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerliazer(instance.company_id).data
        return response
        
class BillDetailsSerliazer(serializers.ModelSerializer):
    class Meta:
        model  = BillDetails
        fields = "__all__"
        
    # To access foreign key data we override method here
    # beacue we have employee_id in BillDetails model
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['bill'] = BillSerliazer(instance.bill_id).data
        return response
