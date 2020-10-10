from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.http import Http404
from django.http import HttpResponse
from .forms import *
from .models import *
from django.core.files.storage import default_storage

# Create your views here.

class CustomerIndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        user = request.POST.get("username")
        customers = Customer.objects.all()

        for customer in customers:
            if str(customer.id) == user:
                return redirect('abcpharma:order_view')

        return HttpResponse("Username does not exist.")
        
class CustomerRegistrationView(View):
    def get(self, request):
        return render(request, 'customerRegistration.html')

    def post(self,request):
        form = CustomerForm(request.POST)

        if form.is_valid():
            profilePic = request.FILES['profile_photo']
            fname = request.POST.get("firstname")
            mname = request.POST.get("middlename")
            lname = request.POST.get("lastname")
            address = request.POST.get("address")
            bday = request.POST.get("birthdate")
            bplace = request.POST.get("birthplace")
            status = request.POST.get("status")
            gender = request.POST.get("gender")
            spouseN = request.POST.get("spouseName")
            spouseO = request.POST.get("spouseOccupation")
            numChild = request.POST.get("numChildren")
            motherN = request.POST.get("motherName")
            motherO = request.POST.get("motherOccupation")
            fatherN = request.POST.get("fatherName")
            fatherO = request.POST.get("fatherOccupation")
            height = request.POST.get("height")
            weight = request.POST.get("weight")
            religion = request.POST.get("religion")
            dateReg = request.POST.get("dateRegistered")

            form = Customer(photo = profilePic, firstname = fname, middlename = mname, lastname = lname, address = address,
                birthDate = bday, birthPlace = bplace, status = status, gender = gender, spouseName = spouseN, 
                spouseOccupation = spouseO, children = numChild, motherName = motherN, motherOccupation = motherO,
                fatherName = fatherN, fatherOccupation = fatherO, height = height, weight = weight, religion = religion, 
                dateRegistered = dateReg)
            form.save()

            return redirect('abcpharma:dashboard_view')
        else:
            print(form.errors)
            return HttpResponse('not valid')

class CustomerOrderView(View):
    def get(self, request):
        medicines = Medicine.objects.all()
        context = {
            'medicines' : medicines
        }
        return render(request, 'orderPage.html', context)

    def post(self, request):

        return

class DashboardIndexView(View):
    def get(self, request):
        customers = Customer.objects.all()
        medicines = Medicine.objects.all()
        context = {
            'customers' : customers,
            'medicines' : medicines
        }
        return render(request, 'dashboard.html', context)
    
    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print('update profile button clicked')
                SKU1 = request.POST.get("SKU")
                category1 = request.POST.get("category")
                genericName1 = request.POST.get("genericName")
                commonBrand1 = request.POST.get("commonBrand")
                manufacturedDate1 = request.POST.get("manufacturedDate")
                expiryDate1 = request.POST.get("expiryDate")
                size1 = request.POST.get("size")
                howToUse1 = request.POST.get("howToUse")
                sideEffects1 = request.POST.get("sideEffects")
                price1 = request.POST.get("price")
                noOfItems1 = request.POST.get("noOfItems")
                print(manufacturedDate1)
                print(noOfItems1)
                print(SKU1)
                update_medicine = Medicine.objects.filter(SKU=SKU1).update(category = category1, genericName = genericName1, commonBrand = commonBrand1, manufacturedDate = manufacturedDate1, expiryDate = expiryDate1, size = size1,
                    howToUse = howToUse1, sideEffects = sideEffects1, price = price1, noOfItems = noOfItems1)
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                SKU1 = request.POST.get("SKU")
                print(SKU1)
                med = Medicine.objects.filter(SKU = SKU1).delete()
                print('Deleted')
        return redirect('abcpharma:dashboard_view')

class MedicineRegistrationView(View):
    def get(self, request):
       # print('get')
        return render(request, 'medReg.html')
    
    def post(self, request):
        form = MedicineForm(request.POST)
        if form.is_valid():
            category1 = request.POST.get("category")
            genericName1 = request.POST.get("genericName")
            commonBrand1 = request.POST.get("commonBrand")
            manufacturedDate1 = request.POST.get("manufacturedDate")
            expiryDate1 = request.POST.get("expiryDate")
            size1 = request.POST.get("size")
            howToUse1 = request.POST.get("howToUse")
            sideEffects1 = request.POST.get("sideEffects")
            price1 = request.POST.get("price")
            noOfItems1 = request.POST.get("noOfItems")
            images = request.FILES['images']
            
            
            form = Medicine(category = category1, genericName = genericName1, commonBrand = commonBrand1, manufacturedDate = manufacturedDate1, expiryDate = expiryDate1, size = size1,
                    howToUse = howToUse1, sideEffects = sideEffects1, price = price1, noOfItems = noOfItems1, images = images)
           
            form.save()
            return redirect('abcpharma:dashboard_view')
        else:
            print(form.errors)
            return HttpResponse("failed")