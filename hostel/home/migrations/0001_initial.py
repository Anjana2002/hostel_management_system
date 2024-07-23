# Generated by Django 5.0.7 on 2024-07-22 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PendingStudentRegistration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('programme', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('aadhaar_number', models.CharField(max_length=12)),
                ('email_id', models.EmailField(max_length=100)),
                ('guardian', models.CharField(max_length=100)),
                ('guardian_number', models.CharField(max_length=15)),
                ('food_preference', models.CharField(max_length=10)),
                ('user_name', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'PendingStudentRegistration',
            },
        ),
        migrations.CreateModel(
            name='programme',
            fields=[
                ('pgm_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pgm_name', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('UG', 'Undergraduate'), ('PG', 'Postgraduate'), ('INT', 'Integrated')], default='UG', max_length=3)),
            ],
            options={
                'db_table': 'programme',
            },
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('role_id', models.IntegerField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('room_id', models.IntegerField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.role')),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('stud_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('aadhaar_number', models.CharField(max_length=12)),
                ('email_id', models.EmailField(max_length=100)),
                ('guardian', models.CharField(max_length=100)),
                ('guardian_number', models.CharField(max_length=15)),
                ('food_preference', models.CharField(max_length=10)),
                ('programme_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.programme')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='warden',
            fields=[
                ('warden_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=10)),
                ('aadhar_no', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('join_date', models.DateField()),
                ('status', models.CharField(choices=[('Working', 'Working'), ('Not Working', 'Not Working')], default='Working', max_length=20)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.role')),
            ],
            options={
                'db_table': 'warden',
            },
        ),
    ]
