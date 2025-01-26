from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


        label = {
            'employee_id' : "Employee ID",
            'name': 'Employee Name',
            'department': 'Department',
            'position': 'Position',
            'floor': 'Floor',
            'salary': 'Salary',

        }


        widgets = {
            'employee_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'floor': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
        }
