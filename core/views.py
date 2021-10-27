from decimal import Context
from typing import Tuple
from django.db.models import query
from django.shortcuts import render, get_list_or_404
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from core import serializers
from core.serializers import(
    EmployeeSerliazer,
    EmployeeSalarySerliazer,
    EmployeeBankSerliazer,
    CustomerSerliazer,
    CustomerRequestSerliazer,
    CompanySerliazer,
    CompanyBankSerliazer,
    CompanyAccountSerliazer,
    MedicineSerliazer,
    MedicineDetailsSerliazer,
    BillSerliazer,
    BillDetailsSerliazer
)
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

# Create your views here.

# Views for comapny
class CompanyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        company = Company.objects.all()
        serializer = CompanySerliazer(company, many=True, context ={"request" : request})
        response_dict = {"error" : False, "message" : "All data of company", "data" :serializer.data}
        return Response(response_dict)
    
    def create(self, request):
        try:
            serializer = CompanySerliazer(context={"request":request}, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error":False, "message":"Company data save successfully"}
        except:
            response_dict = {"error":True, "message":"Error company data is not saved"}
        return Response(response_dict)
    
    
    def retrieve(self, request, pk=None):
        queryset = Company.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerliazer(company, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID
        company_bank_details = CompanyBank.objects.filter(company_id=serializer_data["id"])
        companybank_details_serializers = CompanyBankSerliazer(company_bank_details, many=True)
        serializer_data["company_bank"] = companybank_details_serializers.data

        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})
    
    
    def update(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company  = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerliazer(company, context={"request": request}, data = request.data)
            serializer.is_valid()
            serializer.save()
            response_dict = {"error":False, "message":"Company data updated successfully"}
        except:
            response_dict = {"error":True, "message":"Company data is not update "}
        return Response(response_dict)
    
    
company_list = CompanyViewSet.as_view({"get":"list"})
company_create = CompanyViewSet.as_view({"post":"create"})
company_update = CompanyViewSet.as_view({"put":"update"})
company_retrieve = CompanyViewSet.as_view({"get":"retrieve"})


# Views for company bank
class CompanyBankViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        companybank = CompanyBank.objects.all()
        serializer = CompanyBankSerliazer(companybank, many=True, context ={"request": request})
        response_dict = {"error": False, "message" : "All the company bank data", "data" : serializer.data}
        return Response(response_dict)
    
    def create(self, request):
        try:
            serializer = CompanyBankSerliazer(context= {"request":request}, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error":False, "message" : "Company bank data saved successfully"}
        except:
            response_dict = {"error":True, "message" : "Something wrong"}
        return Response(response_dict)
    
    def retrieve(self, request, pk=None):
        queryset = CompanyBank.objects.all()
        companybank = get_object_or_404(queryset, pk=pk)
        serializer = CompanyBankSerliazer(companybank,context= {"request": request})
        response_dict = {"error":False, "message" : "Single data fetch of bank data", "data":serializer.data}
        return Response(response_dict)
    
    def update(self, request, pk=None):
        try:
            queryset = CompanyBank.objects.all()
            companybank = get_object_or_404(queryset, pk=pk)
            serializer = CompanyBankSerliazer(companybank, context = {"request": request}, data = request.data)
            serializer.is_valid()
            serializer.save()
            response_dict = {"error":False, "message" : "Company bank data updated successfully"}
        except:
            response_dict = {"error":True, "message" : "Company bank data isn't update"}
        return Response(response_dict)


# views to accept the foreign key data (for example here company name)
# Custom filter data
class CompanyNameViewset(ListAPIView):
    serializer_class =CompanySerliazer
    
    def get_queryset(self):
        name = self.kwargs["name"]
        return Company.filter(name=name)
    
    
    
# Views for Medicine
# In this class we are workign with two tables (Medicine, MedicineDetails)
class MedicineViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        medicine = Medicine.objects.all()
        serializer = MedicineSerliazer(medicine, many=True, context ={"request" : request})
        
        medicine_data = serializer.data
        medicinelist = []
        
        for medicine in medicine_data:
            # accessing medicine details of current id
            medicine_details = MedicineDetails.objects.filter(medicine_id = medicine['id'])
            # serialize
            medicine_details_serializer = MedicineDetailsSerliazer(medicine_details, many=True)
            medicine_details["medicine_details"] = medicine_details_serializer.data
            medicinelist.append(medicine_details)
        
        response_dict = {"error" : False, "message" : "All data of medicine", "data" :medicinelist}
        return Response(response_dict)
    
    
    def create(self, request):
        try:
            serializer = MedicineSerliazer(context={"request":request}, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # Here we will send and save the data in two tables (Medicine, MedicineDetails) from one create method 
            medicine_id = serializer.data['id']
            medicine_details_list = []
            # fetch data using for loop
            for medicine_detail in request.data['medicine_details']:
                medicine_detail["medicine_id"] = medicine_id
                medicine_details_list.append(medicine_detail)
            # At first we fetch medicine id (in which id we want to pass medicine id)
            # Then create list to append data
            # Then fetch data from request using key name (key name is 'medicine_details' )
            # Then added the value in that medicine_id
            # Then we append value into list
            # Now serialize it
            serializer2 = MedicineDetailsSerliazer(data= medicine_details_list, context={"request": request}, Many=True)
            serializer2.is_valid()
            serializer2.save()
            response_dict = {"error":False, "message":"Medicine data save successfully"}
        except:
            response_dict = {"error":True, "message":"Error medicine data is not saved"}
        return Response(response_dict)
    
    
    def retrieve(self, request, pk=None):
        queryset = Medicine.objects.all()
        medicine = get_object_or_404(queryset, pk=pk)
        serializer = MedicineSerliazer(medicine,context= {"request": request})
        
        serializer_data = serializer.data
        # fetch deatils of currend id
        medicine_details = MedicineDetails.objects.filter(medicine_id = serializer_data["id"])
        # seriralzie data
        medicine_details_serializer = MedicineDetailsSerliazer(medicine_details, many=True)
        serializer_data["medicine_details"] = medicine_details_serializer.data
        response_dict = {"error":False, "message" : "Single data fetch of medicine", "data":serializer_data}
        return Response(response_dict)
    
    
    def update(self, request, pk=None):
        try:
            queryset = Medicine.objects.all()
            medicine  = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerliazer(medicine, context={"request": request}, data = request.data)
            serializer.is_valid()
            serializer.save()
            response_dict = {"error":False, "message":"Medicine data updated successfully"}
        except:
            response_dict = {"error":True, "message":"MEdicine data is not update "}
        return Response(response_dict)