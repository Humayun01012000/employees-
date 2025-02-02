from django.db import models




# Employee Model
class Employee(models.Model):
    employee_id = models.PositiveBigIntegerField(unique=True)  # Ensure unique Employee ID
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    position =  models.CharField(max_length=100)
    floor = models.CharField(max_length=100)
    salary = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.department.name} - {self.position.name}"


