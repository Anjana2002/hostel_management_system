# Generated by Django 5.0.7 on 2024-07-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_student_programme_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
