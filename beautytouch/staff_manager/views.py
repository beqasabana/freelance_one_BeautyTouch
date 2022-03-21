from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Employee
# Create your views here.

def index(request):
    if 'logged_user' in request.session:
        return redirect('/staff/dashboard')
    else:
        return render(request, 'signin.html')

def login(request):
    user_info = {
        'user_name': request.POST['user_name'],
        'password': request.POST['password']
    }
    emp, errors = Employee.objects.validate_login(user_info)
    if emp == 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/staff')
    else:
        request.session['logged_user'] = emp.id
        return redirect(f"/staff/dashboard")

def dashboard(request):
    try:
        context = {
            'logged_user': Employee.objects.get(id=request.session['logged_user'])
        }
        return render(request, 'staff_dashboard.html', context)
    except KeyError:
        return redirect('/staff')

def logout(request):
    if not 'logged_user' in request.session:
        return redirect('/staff')
    else:
        request.session.clear()
        return redirect('/staff')