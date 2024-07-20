from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login as auth_login
from .models import login
# Create your views here.


def HomeView(request):
    return render(request, 'home.html')

def login_home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = login.objects.get(username=username, password=password)
        except login.DoesNotExist:
            user = None

        if user is not None:
            # Set user session manually
            request.session['user_id'] = user.user_id
            request.session['role_id'] = user.role_id.role_id
            request.session['username'] = user.username

            if user.role_id.role_id == 1:
                return redirect('admin_index')
            else:
                return redirect('warden_index')  
        else:
            return render(request, 'home.html', {'error': 'Invalid username or password'})
    
    return render(request, 'home.html')

def admin_view(request):
    return render(request, 'admin/admin_index.html')

def warden_view(request):
    username = request.session.get('username')
    username = username.capitalize()
    context={
        'username':username
    }
    return render(request, 'warden/warden_index.html', context)

def add_student(request):
    return render(request, 'warden/add_student.html')

def attendance(request):
    return render(request, 'warden/attendance.html')

def attendance_rep(request):
    return render(request, 'warden/attendance_rep.html')