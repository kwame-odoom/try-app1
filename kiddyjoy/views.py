from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'kidJoy/index.html')

def donate(request):
    #if request.method == 'POST':
    return render(request, 'kidJoy/donate.html')

def team(request):
    return render(request, 'kidJoy/team.html')

def about(request):
    return render(request, 'kidJoy/about.html')

def join_team(request):
    return render(request, 'kidJoy/join-team.html')

def contact(request):
    return render(request, 'kidJoy/contact.html')

def all_projects(request):
    return render(request, 'kidJoy/all-projects.html')

def past_projects(request):
    return render(request, 'kidJoy/past-projects.html')

def upcoming_projects(request):
    return render(request, 'kidJoy/upcoming-projects.html')

def ongoing_projects(request):
    return render(request, 'kidJoy/ongoing-projects.html')