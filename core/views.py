from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.models import UserProfileModel, Feedback, TrainingProgramModel, AppreciationPoints
from core.models import Notification
from users.forms import UserProfileForm
from django.utils import timezone
from django.contrib.auth import get_user_model
from core.forms import TrainingProgramForm
from django.contrib import messages
from core.forms import AppreciationPointsForm

User = get_user_model()




def send_points(request):
    # Fetch all AppreciationPoints objects
    all_points = AppreciationPoints.objects.all().order_by('-created_at')  # Sorting by creation date
    data = {'all_points': all_points}
    return render(request, 'send_points.html', data)


def add_training(request):
    if request.method == 'POST':
        form = TrainingProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:emp_trainings')  # Redirect to training list page or another page
    else:
        form = TrainingProgramForm()

    return render(request, 'add_trainings.html', {'form': form})


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
    trainings = TrainingProgramModel.objects.all()
    profile = UserProfileModel.objects.filter(user=request.user)[0]
    data = {"trainings":trainings,"profile":profile}
    print(trainings)
    return render(request, 'trainings.html',data)



@login_required
def promotion(request):
    return render(request, 'promotion.html')

def recognition_view(request):
    sender_profile = UserProfileModel.objects.get(user=request.user)
    # Sort profiles by points in descending order for the leaderboard
    profiles = UserProfileModel.objects.all().order_by('-points')[:3]

    if request.method == 'POST':
        form = AppreciationPointsForm(request.POST)
        if form.is_valid():
            receiver = form.cleaned_data['receiver']
            points = form.cleaned_data['points']

            # Check if the sender has enough points
            if sender_profile.points >= points:
                print(points)
                

                # Deduct the points from sender's profile
                sender_profile.points -= points
                sender_profile.save()

                # Add the points to the receiver's profile
                receiver.points += points
                receiver.save()

                messages.success(request, 'Points successfully sent!')
                return redirect('core:emp_rewards')
            else:
                messages.error(request, 'You do not have enough points to send.')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = AppreciationPointsForm()

    data = {'profiles': profiles,'form': form}
    return render(request, 'rewards.html',data)

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


@login_required
def feedback_view(request):
    # Handle form submission
    if request.method == 'POST':
        feedback_type = request.POST.get('feedback-type')
        feedback_message = request.POST.get('feedback-message')
        title = f"{feedback_type.capitalize()} Feedback"
        
        # Create feedback object
        feedback = Feedback(
            user=request.user,  # Assuming user is logged in
            title=title,
            feedback=feedback_message,
            time=timezone.now()
        )
        feedback.save()

        return redirect('core:feedback')

    # Get all feedbacks for the logged-in user
    feedback_list = Feedback.objects.filter(user=request.user).order_by('-time')
    feedback_all = Feedback.objects.all()

    # Render the template with feedback data
    return render(request, 'feedback.html', {'feedback_list': feedback_list,"feedback_all":feedback_all})



@login_required
def notification_center(request):
    users = User.objects.exclude(id=request.user.id)  # Get all users except the logged-in user
    received_notifications = Notification.objects.filter(receiver=request.user).order_by('-created_at')
    sent_notifications = Notification.objects.filter(sender=request.user).order_by('-created_at')

    if request.method == "POST":
        receiver_id = request.POST.get("receiver")
        message = request.POST.get("message")

        if receiver_id and message:
            receiver = User.objects.get(id=receiver_id)
            Notification.objects.create(sender=request.user, receiver=receiver, message=message)
            return redirect("core:notification_center")  # Redirect to refresh the page

    return render(request, "notification_center.html", {
        "users": users,
        "received_notifications": received_notifications,
        "sent_notifications": sent_notifications,
    })

