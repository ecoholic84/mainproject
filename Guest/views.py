from django.shortcuts import render

# Create your views here.
def userRegistration(request):
    return render(request,'Guest/userRegistration.html')
