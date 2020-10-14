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
        form = LoginForm(request.POST)

        for customer in customers:
            if str(customer.id) == user and customer.isDeleted != 1:                
                if form.is_valid():
                    username1 = request.POST.get("username")
                    form = Login.objects.get(id=1)
                    form.username = username1
                    form.save()   
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
        medicines = Medicine.objects.filter(isDeleted = 0)
        currentUser = Login.objects.values_list("username", flat=True).get(pk = 1)
        orders = Order.objects.filter(customer_id = currentUser)
        
        customers = Customer.objects.filter(person_ptr_id = currentUser)
        context = {
            'medicines' : medicines,
            'customers' : customers,
            'orders' : orders
        }
        return render(request, 'orderPage.html', context)

    def post(self, request):
        form = OrderForm(request.POST)
        SKU = request.POST.get("SKU")
        orders = Order.objects.all()
        currentUser = Login.objects.values_list("username", flat=True).get(pk = 1)

        if request.method == 'POST':
            if 'btnBuy' in request.POST:
                number = request.POST.get("noOfItems")
                quantity = request.POST.get("quantity")
                dif = int(number) - int(quantity)
                if form.is_valid():
                    for order in orders:
                        if(int(order.medicine_id) == int(SKU) and int(order.customer_id) == int(currentUser)):
                            quantity1 = int(order.quantity) + int(quantity)                                             
                            update_quantity = Order.objects.filter(id = order.id).update(quantity = quantity1)
                            update_quantity = Medicine.objects.filter(SKU = SKU).update(noOfItems = dif)
                            return redirect('abcpharma:order_view')
                    
                    form = Order(medicine_id = SKU, customer_id = currentUser, quantity = quantity)
                    update_quantity = Medicine.objects.filter(SKU = SKU).update(noOfItems = dif)
                    form.save()                             
                return redirect('abcpharma:order_view')
                
                
                

                
                


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
            if 'btnUpdateMedicine' in request.POST:
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
            elif 'btnDeleteMedicine' in request.POST:
                print('delete button clicked')
                SKU1 = request.POST.get("SKU")
                print(SKU1)
                med = Medicine.objects.filter(SKU = SKU1).update(isDeleted = 1)
                print('Deleted')
            elif 'btnUpdateCustomer' in request.POST:
                customerID = request.POST.get("customer-id")
                fname = request.POST.get("customer-firstname")
                mname = request.POST.get("customer-middlename")
                lname = request.POST.get("customer-lastname")
                address = request.POST.get("customer-address")
                bday = request.POST.get("customer-birthdate")
                bplace = request.POST.get("customer-birthplace")
                status = request.POST.get("customer-status")
                gender = request.POST.get("customer-gender")
                spouseN = request.POST.get("customer-spousename")
                spouseO = request.POST.get("customer-spouseoccupation")
                numChild = request.POST.get("customer-children")
                motherN = request.POST.get("customer-mothername")
                motherO = request.POST.get("customer-motheroccupation")
                fatherN = request.POST.get("customer-fathername")
                fatherO = request.POST.get("customer-fatheroccupation")
                height = request.POST.get("customer-height")
                weight = request.POST.get("customer-weight")
                religion = request.POST.get("customer-religion")

                update_customer = Customer.objects.filter(person_ptr_id = customerID).update(firstname = fname, 
                    middlename = mname, lastname = lname, address = address, birthDate = bday, birthPlace = bplace, 
                    status = status, gender = gender, spouseName = spouseN, spouseOccupation = spouseO, children = numChild, 
                    motherName = motherN, motherOccupation = motherO, fatherName = fatherN,  fatherOccupation = fatherO, 
                    height = height, weight = weight, religion = religion)
                print(update_customer)
            elif 'btnDeleteCustomer' in request.POST:
                customerID = request.POST.get("customerr-id")
                customerr = Customer.objects.filter(person_ptr_id = customerID).update(isDeleted = 1)
                #personn = Person.objects.filter(id = customerID).delete()
                
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
            #test
