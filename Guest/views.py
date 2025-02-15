from django.shortcuts import render
from Admin.models import *

# Create your views here.
def userRegistration(request):
    dis=tbl_district.objects.all()
    return render(request,'Guest/userRegistration.html', {"district":dis})