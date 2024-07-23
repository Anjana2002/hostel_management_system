from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login as auth_login
from .models import login, student, PendingStudentRegistration, programme, role
from .forms import StudentRegistrationForm
from django.contrib import messages
# Create your views here.




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

def stud_reg(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            pending_student = PendingStudentRegistration(
                name=form.cleaned_data['name'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                programme=form.cleaned_data['programme'],
                phone_number=form.cleaned_data['phone_number'],
                address=form.cleaned_data['address'],
                aadhaar_number=form.cleaned_data['aadhaar_number'],
                email_id=form.cleaned_data['email_id'],
                guardian=form.cleaned_data['guardian'],
                guardian_number=form.cleaned_data['guardian_number'],
                food_preference=form.cleaned_data['food_preference'],
                user_name=form.cleaned_data['user_name'],
                password=form.cleaned_data['password']
            )
            pending_student.save()
            messages.success(request, 'Your registration is pending approval. We will contact you soon.')
            return redirect('registration_success')
    else:
        form = StudentRegistrationForm()
    return render(request, 'stud_reg.html', {'form': form})

def registration_success(request):
    return render(request, 'registration_success.html')

def admin_view(request):
    return render(request, 'admin/admin_index.html')


def approve_student(request):
    pending_students = PendingStudentRegistration.objects.filter(is_approved=False)
    return render(request, 'warden/approve_student.html',{'pending_students':pending_students})

def get_next_user_id():
    # Fetch the last user_id, if any
    last_login =login.objects.last()
    
    if last_login:
        # Increment the last user_id
        return last_login.user_id + 1
    else:
        # Start with 1 if there are no records
        return 1
    
def approving(request, student_id):
    if request.method=="POST":
        pending = get_object_or_404(PendingStudentRegistration, id=student_id)
        action = request.POST.get('action')
        if action=='approve':
            
            programme_instance = get_object_or_404(programme, pgm_name=pending.programme)
            new_student = student.objects.create(
                name = pending.name,
                date_of_birth = pending.date_of_birth,
                programme_id=programme_instance,
                phone_number=pending.phone_number,                    
                address=pending.address,
                aadhaar_number=pending.aadhaar_number,
                email_id=pending.email_id,
                guardian=pending.guardian,
                guardian_number=pending.guardian_number,
                food_preference=pending.food_preference

            )
            
            student_role = get_object_or_404(role, pk=3)
            new_user_id = get_next_user_id()
            login.objects.create(
                user_id=new_user_id,
                username = pending.user_name,
                password = pending.password,
                role_id = student_role
            )
            
            pending.delete()
            messages.success(request, f'Student {pending.name} has been approved.')
           
        elif action == 'deny':
            try:
                pending.delete()
                messages.success(request, f'Student application for {pending.name} has been denied.')
            except Exception as e:
                messages.error(request, f'Error denying student application: {str(e)}')
        
        else:
            messages.error(request, 'Invalid action.')

    return redirect('approve_student')



def warden_view(request):
    username = request.session.get('username')
    username = username.capitalize()
    context={
        'username':username
    }
    return render(request, 'warden/warden_index.html', context)



def attendance(request):
    return render(request, 'warden/attendance.html')

def attendance_rep(request):
    return render(request, 'warden/attendance_rep.html')

