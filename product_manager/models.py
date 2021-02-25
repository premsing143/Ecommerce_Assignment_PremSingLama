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
