from django.db import models

# Create your models here. 


class Employee(models.Model):
    employee_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    floor = models.CharField(max_length=100)
    salary = models.FloatField()
 
    def __str__(self):
        return f"Name: {self.name} Department: {self.department}"