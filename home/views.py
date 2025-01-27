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


def employee_int(request, id):
    employee = Employee.objects.get(id=id)
    context = {
        'employees': employee,
    }
    return render(request, 'home/employee_int.html', context)


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


def edit_employee(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect(reverse('home:employee'))
    context = {'form': form, 'employee': employee}
    return render(request, 'home/edit_employee.html', context) 


def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
       employee.delete()
       return redirect(reverse('home:employee'))
    return render(request, 'home/delete_employee.html',)
    