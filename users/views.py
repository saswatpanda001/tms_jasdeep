from django.shortcuts import render, redirect
from allauth.account.views import LoginView
from django.contrib.auth.decorators import login_required
from users.models import UserProfileModel

class EmployeeLoginView(LoginView):
    template_name = "account/employee_login.html"

class ManagerLoginView(LoginView):
    template_name = "account/manager_login.html"

class HrManagerLoginView(LoginView):
    template_name = "account/hr_login.html"


@login_required
def role_based_redirect(request):
    user = request.user
    profile_data = UserProfileModel.objects.filter(user=user)
    if len(profile_data)==0:
        return redirect("users:login_dashboard")
    else:
        profile_data = profile_data[0]
        if profile_data.role=="employee":
            return redirect('users:employee_dashboard')
        elif profile_data.role=="manager":
            return redirect('users:manager_dashboard')
        elif profile_data.role=="hr_manager":
            return redirect('users:hrmanager_dashboard')
        else:
            return redirect('/users/login')
        
   


def login_dashboard(request):
    return render(request,"login_dashboard.html")


def employee_dashboard(request):
    return render(request,"employee_dashboard.html")


def manager_dashboard(request):
    return render(request,"manager_dashboard.html")


def hrmanager_dashboard(request):
    return render(request,"hr_dashboard.html")