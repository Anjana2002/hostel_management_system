from django.db import models

# Create your models here.
class role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=10)
    class Meta:
        db_table = 'role'

class warden(models.Model):
    WORKING = 'Working'
    NOT_WORKING = 'Not Working'
    STATUS_CHOICES = [
        (WORKING, 'Working'),
        (NOT_WORKING, 'Not Working'),
    ]
     
    warden_id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey(role, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    aadhar_no = models.CharField(max_length=12)
    address = models.TextField()
    join_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Working')
    class Meta:
        db_table = 'warden'


class login(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    role_id = models.ForeignKey(role, on_delete=models.CASCADE)
    class Meta:
        db_table = 'login'