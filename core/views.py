from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard_emp.html')


def dashboard_mng(request):
    return render(request, 'dashboard_manager.html')


def feedback(request):
    return render(request, 'feedback.html')

def learning(request):
    return render(request, 'learning.html')

def promotion(request):
    return render(request, 'promotion.html')

def rewards(request):
    return render(request, 'rewards.html')

def skillgap(request):
    return render(request, 'skillgap.html')

def promotion(request):
    return render(request, 'promotion.html')

def profile(request):
    return render(request, 'profile.html')
