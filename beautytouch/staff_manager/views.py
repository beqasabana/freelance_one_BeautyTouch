from django.shortcuts import render, HttpResponse
from .models import Employee
# Create your views here.

def index(request):
    return render(request, 'signin.html')

def login(request):
    user_info = {
        'user_name': request.POST['user_name'],
        'password': request.POST['password']
    }
    emp = Employee.objects.validate_login(user_info)
    print(emp)
    return HttpResponse('fail')