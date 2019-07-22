from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField(label='البريد الالكتروني', widget=forms.EmailInput(attrs={
        'class':"form-control mb-4",
        'placeholder':'البريد الالكتروني'
        }))
    password = forms.CharField(label='كلمة المرور',widget=forms.PasswordInput(attrs={
        'class':"form-control mb-4",
        'placeholder':'كلمة المرور'
        }))


class SignupForm(forms.Form):
    username = forms.CharField(label='إسم المستخدم',widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='البريد الالكتروني',widget=forms.EmailInput(attrs={'class':"form-control mb-4"}))
    password = forms.CharField(label='كلمة المرور',widget=forms.PasswordInput(attrs={'class':"form-control mb-4"}))
    password_repeat = forms.CharField(label='تأكيد كلمة المرور',widget=forms.PasswordInput(attrs={'class':"form-control mb-4"}))
    first_name = forms.CharField(label='الإسم الاول',widget=forms.TextInput(attrs={'class':"form-control mb-4"}))
    last_name = forms.CharField(label='اللقب',widget=forms.TextInput(attrs={'class':"form-control mb-4"}))
    phone_number = forms.CharField(label='الهاتف',widget=forms.NumberInput(attrs={'class':"form-control mb-4"}), required=False)

