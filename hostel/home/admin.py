
from django.contrib import admin
from .models import role, login, warden, PendingStudentRegistration, programme, student, room

# Register your models here.
admin.site.register(role)
admin.site.register(login)
admin.site.register(warden)
admin.site.register(PendingStudentRegistration)
admin.site.register(programme)
admin.site.register(student)
admin.site.register(room)