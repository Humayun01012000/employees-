from django.shortcuts import render,redirect 

from django.urls import reverse

from .models import Employee

from .forms import EmployeeForm
# Create your views here.

def index(request):
    return render(request, 'home/index.html') 


def employee(request):
    employees = Employee.objects.all()
   
    context = {
        'employees': employees,  # Passing the list of employees to the template
         
    }
    return render(request, 'home/employee.html', context)

def employee_details(request):
    employees = Employee.objects.all()
    context ={
        'employees': employees,  # Passing the list of employees to the template
    }
    return render(request, 'home/details.html', context)

def add_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            new_employee_id = form.cleaned_data['employee_id']
            new_name = form.cleaned_data['name']
            new_department = form.cleaned_data['department']
            new_position = form.cleaned_data['position']
            new_floor = form.cleaned_data['floor']
            new_salary = form.cleaned_data['salary']

            new_employee = Employee(employee_id = new_employee_id, name =new_name, department=new_department,position =new_position , floor=new_floor, salary=new_salary)


            new_employee.save()
            return redirect(reverse('home:employee'))
    context = {'form': form}
    return render(request, 'home/add_employee.html', context)
    