from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("", views.index, name="home"),
    path("employee/", views.employee, name="employee"),
    path("employee_details/", views.employee_details, name="details"),
    path("add_employee/", views.add_employee, name="add_employee"),
]