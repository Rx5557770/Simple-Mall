from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout

# from rest_framework import viewsets, permissions
# from django.contrib.auth import get_user_model
#
# from .serializer import AccountSerializer

# User = get_user_model()
#
# class AccountViewSet(viewsets.ModelViewSet):
#     model = User
#     permission_classes = (permissions.IsAdminUser, )
#     queryset = User.objects.all()
#     serializer_class = AccountSerializer


class LoginView(View):
    def get(self,request):
        pass
    def post(self,request):
        pass


class RegisterView(View):
    def get(self,request):
        pass
    def post(self,request):
        pass


class LogoutView(View):
    def post(self,request):
        logout(request)