from django.urls import path, include
from .import views

urlpatterns = [
    # path('',views.HomeView, name="home"),
    path('', views.login_home, name='login_home'),
    path('stud_reg/', views.stud_reg, name='stud_reg'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('admin_hostel/', views.admin_view, name='admin_index'),
    path('warden/',views.warden_view, name='warden_index'),
    
    path('warden/approve_student', views.approve_student, name='approve_student'),
    path('warden/approving/<int:student_id>/', views.approving, name='approving'),
    path('warden/attendance/', views.attendance, name='attendance'),
    path('warden/attendance_rep/', views.attendance_rep, name='attendance_rep')
]
    