from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("", views.index, name="home"),
    path("employee/", views.employee, name="employee"),
    path("employee/<int:id>/", views.employee_int, name="employee_int"),
    path("employee_details/", views.employee_details, name="details"),
    path("add_employee/", views.add_employee, name="add_employee"),
    path("edit_employee/<int:id>/", views.edit_employee, name="edit_employee"),
    path("delete_employee/<int:id>/", views.delete_employee, name="delete_employee"),
    # path("search_employee/", views.search_employee, name="search_employee"),
    # path("logout/", views.logout_view, name="logout"),
    # path("login/", views.login_view, name="login"),
]