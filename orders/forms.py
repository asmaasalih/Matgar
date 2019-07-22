from django import forms
from .models import order

class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='الإسم الاول', widget=forms.TextInput(attrs={
        'class':"form-control mb-4"
        }))
    last_name = forms.CharField(label='اللقب', widget=forms.TextInput(attrs={
        'class':"form-control mb-4"
        })) 
    email = forms.EmailField(label='البريد الالكتروني', widget=forms.EmailInput(attrs={
        'class':"form-control mb-4"
        })) 
    city =  forms.CharField(label='المدينة', widget=forms.TextInput(attrs={
        'class':"form-control mb-4"
        })) 
    region = forms.CharField(label='المنطقة', widget=forms.TextInput(attrs={
        'class':"form-control mb-4"
        })) 
    address = forms.CharField(label='العنوان', widget=forms.TextInput(attrs={
        'class':"form-control mb-4"
        }))               
    CHOICES = [('1', 'PayPal')]
    payment_method = forms.ChoiceField(label="طريقة الدفع",widget=forms.RadioSelect,choices=CHOICES)

    class Meta:
        model = order
        fields = ('first_name','last_name','email','address','city','region','payment_method')