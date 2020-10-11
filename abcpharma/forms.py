from django import forms
from .models import *

class CustomerForm(forms.ModelForm):

	class Meta:
		model = Customer
		fields = ('firstname','lastname','address','status','gender','motherName',
			'motherOccupation','fatherName','fatherOccupation','height','weight')
		
class MedicineForm(forms.ModelForm):
    
    class Meta:
        model = Medicine
        fields = ('category','genericName')

class OrderForm(forms.ModelForm):

	class Meta:
		model = Order
		fields = ('orderedDate', 'quantity')

class LoginForm(forms.ModelForm):

	class Meta:
		model = Login
		fields = ('username',)