from django.urls import path, include
from .import views
from .views import HomeView
urlpatterns = [
    path('',views.HomeView, name="home"),
    path('login/', views.login_home, name='login_home'),
    path('admin/', views.admin_view, name='admin_index'),
    path('warden/',views.warden_view, name='warden_index'),
    path('warden/add_student/', views.add_student, name='add_student'),
    path('warden/attendance/', views.attendance, name='attendance'),
    path('warden/attendance_rep/', views.attendance_rep, name='attendance_rep')
]
    