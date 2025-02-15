from django.shortcuts import render
from Admin.models import *
from Guest.models import *
# Create your views here.
def userRegistration(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        tbl_user.objects.create(user_name=request.POST.get('txt_name'), user_email=request.POST.get('txt_email'),user_contact=request.POST.get('txt_contact'),user_address=request.POST.get('txt_address'),user_password=request.POST.get('txt_password'), place=tbl_place.objects.get(id=request.POST.get('sel_place')), user_photo=request.FILES.get('txt_photo'))
    return render(request,'Guest/userRegistration.html', {"district":dis})

def ajaxPlace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/ajaxPlace.html', {"place":place})
