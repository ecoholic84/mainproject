from django.shortcuts import render

# Create your views here.
def userDashboard(request):
    return render(request,'User/userDashboard.html')