from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .form import LoginForm, RegisterForm

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'auth/login.html',{'form':form})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['remember']
            user = authenticate(request, username=email, password=password)
            if user:
                login(request,user)
                if not remember:
                    request.session.set_expiry(0)
                return redirect('home:index')
            else:
                form.add_error(None, '账号或密码错误')
        return render(request,'auth/login.html',{'form':form})


class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'auth/register.html',{'form':form})

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:index')
        return render(request,'auth/register.html',{'form':form})


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home:index')