
from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path('login/employee/', views.EmployeeLoginView.as_view(), name='employee_login'),
    path('login/manager/', views.ManagerLoginView.as_view(), name='manager_login'),
    path('login/hrmanager/', views.HrManagerLoginView.as_view(), name='hrmanager_login'),
    path('role_login/', views.role_based_redirect, name='role_redirect'),

    path('login', views.login_dashboard,name='login_dashboard'),
    path('employee', views.employee_dashboard,name='employee_dashboard'),
    path('manager', views.manager_dashboard,name='manager_dashboard'),
    path('hrmanager', views.hrmanager_dashboard,name='hrmanager_dashboard'),
]