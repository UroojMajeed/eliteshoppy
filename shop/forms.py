from django.db.models import fields
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField 
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
class addproduct(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'
class addcontact(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
class addcontact1(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
class CustomerRegistraionForm(UserCreationForm):
 password1 = forms.CharField(label='Password (atleast 8 characters)' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
 password2 = forms.CharField(label='Confirm Password (again)' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
 email = forms.CharField(required=True , widget=forms.EmailInput(attrs={'class':'form-control'}))
 class Meta:
     model = User
     fields = ['username','email','password1','password2']
     labels = {'email':'Email'}
     widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}
class LoginForm(AuthenticationForm):
 username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
 password = forms.CharField(label=_("Password"), strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','phone','email','address','city','postal_code','state']
        widgets = {'name':forms.TextInput(attrs=
        {'class':'form-control'}), 'phone':forms.TextInput(attrs=
        {'class':'form-control'}), 'email':forms.TextInput(attrs=
        {'class':'form-control'}), 'address':forms.TextInput(attrs=
        {'class':'form-control'}), 'city':forms.TextInput(attrs=
        {'class':'form-control'}), 'postal_code':forms.TextInput(attrs=
        {'class':'form-control'}), 'state':forms.TextInput(attrs=
        {'class':'form-control'})}
