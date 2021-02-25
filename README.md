# Ecommerce_Assignment_PremSingLama
###It's a simple project with CRUD Operation
###Project Documentation!!
####step-1:Initialize Django Project
django-admin startproject yourprojectname 
cd ecommerce_yourname

####Step-2:Ensure in Database as
python manage.py migrate 
python manage.py createsuperuser

####Step-3:Add a Module
python manage.py startapp product_module

####Step-4: Install the app in settings.py
INSTALLED_APPS = [ ...,
'product_module' ]

####Step-5: Create the model in models.py
from django.db import models

# Create your models here.
class LabExam(models.Model):
    id=models.IntegerField(primary_key=True)
    exam_date=models.DateField(auto_now_add=True)
    exam_name=models.CharField(max_length=200)
    exam_description=models.TextField(max_length=200)
    total_marks=models.FloatField()
    pass_mark=models.FloatField()
    exam_status=models.BooleanField(default=True)

####Step-6:Ensure in database by migrating
python manage.py makemigrations
python manage.py migrate

####Step-7: Register in admin site
from .models import LabExam
admin.site.register(LabExam)

####Step-8: Run the server:
python manage.py runserver
