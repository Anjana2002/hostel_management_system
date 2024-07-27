from django.db import models

# Create your models here.
class role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=10)
    class Meta:
        db_table = 'role'

class room(models.Model):
    room_id = models.IntegerField(primary_key=True)
    room_name = models.CharField(max_length=10)
    no_of_bed = models.IntegerField(default=4)
    class Meta:
        db_table = 'room'


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

class programme(models.Model):
    UG = 'UG'
    PG = 'PG'
    INT = 'INT'
    
    TYPE_CHOICES = [
        (UG, 'Undergraduate'),
        (PG, 'Postgraduate'),
        (INT, 'Integrated'),
    ]
    
    pgm_id = models.IntegerField(primary_key=True)
    pgm_name = models.CharField(max_length=20)
    type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default=UG,
    )
    class Meta:
        db_table = 'programme'
    def __str__(self):
        return self.pgm_name
        
class PendingStudentRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    programme = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    aadhaar_number = models.CharField(max_length=12)
    email_id = models.EmailField(max_length=100)
    guardian = models.CharField(max_length=100)
    guardian_number = models.CharField(max_length=15)
    food_preference = models.CharField(max_length=10)
    user_name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)  # We'll store the password hash
    is_approved = models.BooleanField(default=False)
 
    class Meta:
        db_table = 'PendingStudentRegistration'
    def __str__(self):
        return self.name
    
class student(models.Model):
    stud_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    programme_id = models.ForeignKey('programme', on_delete=models.CASCADE, null=True, blank=True, db_column='programme_id')
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    aadhaar_number = models.CharField(max_length=12)
    email_id = models.EmailField(max_length=100)
    guardian = models.CharField(max_length=100)
    guardian_number = models.CharField(max_length=15)
    food_preference = models.CharField(max_length=10)
    room = models.ForeignKey('room', on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        db_table = 'student'

class login(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    role_id = models.ForeignKey(role, on_delete=models.CASCADE)
    class Meta:
        db_table = 'login'
    