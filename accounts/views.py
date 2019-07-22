from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .form import SignupForm, LoginForm
from .models import Profile

def signup_view(request):
    template = 'registration/signup.html'
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form, 
                    'error_message': 'إسم المستخدم موجود بالفعل .'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request,template,{
                    'form':form,
                    'error_message':'هذا البريد الالكتروني مستخدم بالفعل '
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request,template,{
                    'form':form,
                    'error_message':'كلمة المرور ليست متطابقه'
               })  
            else:
                user = User.objects.create_user(
                    form.cleaned_data['username'], 
                    form.cleaned_data['email'], 
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
                login(request,user)
                return redirect('shop:home')
    else:
        form = SignupForm()
    return render(request,template,{'form':form})

def login_view(request):
    template = 'registration/login.html'
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    print("user logged in ")
    if form.is_valid():
        print(form.cleaned_data)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('shop:home')
            else:
                print('error message')
        else:
            print('error2')        

    return render(request,template,context)    
    

def my_profile(request):
    template = 'registeration/profile.html'
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
    context = {
        'my_orders': my_orders
	}

    return render(request, template, context)

