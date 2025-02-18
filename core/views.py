from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.models import UserProfileModel
from users.forms import UserProfileForm

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    user = request.user
    if user.last_name =="employee":
        return render(request, 'dashboard_emp.html')
    elif user.last_name=="manager":
        return render(request, 'dashboard_manager.html')
    elif user.last_name=="hr_manager":
        return render(request, 'dashboard_hr.html')
        
@login_required
def dashboard_mng(request):
    return render(request, 'dashboard_manager.html')


@login_required
def feedback(request):
    return render(request, 'feedback.html')

@login_required
def talent(request):
    return render(request, 'talent.html')


@login_required
def reports(request):
    return render(request, 'reports.html')



@login_required
def learning(request):
    return render(request, 'learning.html')


@login_required
def trainings(request):
    return render(request, 'trainings.html')



@login_required
def promotion(request):
    return render(request, 'promotion.html')

@login_required
def rewards(request):
    return render(request, 'rewards.html')

@login_required
def skillgap(request):
    return render(request, 'skillgap.html')

@login_required
def promotion(request):
    return render(request, 'promotion.html')

@login_required
def profile(request):
    profiles = UserProfileModel.objects.filter(user=request.user)
    if len(profiles)==0:
        return render(request,"error.html")
    else:
        profile = profiles[0]
        data = {"userprofile":profile}

    return render(request, 'profile.html',data)

@login_required
def employee_list(request):
    profiles = UserProfileModel.objects.all()
    data = {"profiles":profiles}
    print(profiles)
    return render(request, 'employee_list.html',data)

@login_required
def employee_details(request,id):
    profiles = UserProfileModel.objects.filter(user__id=id)
    if len(profiles)==0:
        return render(request,"error.html")
    else:
        profile = profiles[0]
        data = {"userprofile":profile}
        return render(request, 'employee_details.html',data)




@login_required
def edit_profile(request,id):
    profile = UserProfileModel.objects.get(user__id=id)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("core:emp_details", request.user.id)  # Redirect to profile view
    else:
        form = UserProfileForm(instance=profile)

    return render(request, "edit_profile.html", {"form": form})
