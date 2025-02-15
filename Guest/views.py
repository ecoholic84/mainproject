from django.shortcuts import render
from Admin.models import *

# Create your views here.
def userRegistration(request):
    dis=tbl_district.objects.all()
    return render(request,'Guest/userRegistration.html', {"district":dis})

def ajaxPlace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/ajaxPlace.html', {"place":place})