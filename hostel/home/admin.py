
from django.contrib import admin
from .models import role, login, warden

# Register your models here.
admin.site.register(role)
admin.site.register(login)
admin.site.register(warden)