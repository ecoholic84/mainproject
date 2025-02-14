from django.shortcuts import render,redirect
from Admin.models import *
# Create your views here.

# District Section
def district(request):
    district=tbl_district.objects.all()
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get('txt_district'))
        return redirect('Admin:district')
    else:    
        return render(request,'Admin/District.html',{"district":district})
def deletedistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('Admin:district')
def editdistrict(request,eid):
    dist=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        dist.district_name=request.POST.get('txt_district')
        dist.save()
        return redirect('Admin:district')
    else:    
        return render(request,'Admin/District.html',{"editdist":dist})

# Category Section
def category(request):
    category=tbl_category.objects.all()
    if request.method=="POST":
        tbl_category.objects.create(category_name=request.POST.get('txt_category'))
        return redirect('Admin:category')
    else:
        return render(request,'Admin/Category.html',{"category":category})
def deletecategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect('Admin:category')
def editcategory(request,eid):
    cat=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        cat.category_name=request.POST.get('txt_category')
        cat.save()
        return redirect('Admin:category')
    else:
        return render(request,'Admin/Category.html',{"editcat":cat})


# Admin Section
def AdminRegistration(request):
    admin=tbl_admin.objects.all()
    if request.method=="POST":
        tbl_admin.objects.create(admin_name=request.POST.get('txt_name'),admin_contact=request.POST.get('txt_contact'),admin_email=request.POST.get('txt_email'),admin_password=request.POST.get('txt_password'))
        return redirect('Admin:adminregistration')
    else:
        return render(request,'Admin/AdminRegistration.html',{"admin":admin})
def deleteadmin(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect('Admin:adminregistration')
def editadmin(request,eid):
    adm=tbl_admin.objects.get(id=eid)
    if request.method=="POST":
        adm.admin_name=request.POST.get('txt_name')
        adm.admin_contact=request.POST.get('txt_contact')
        adm.admin_email=request.POST.get('txt_email')
        adm.admin_password=request.POST.get('txt_password')
        adm.save()
        return redirect('Admin:adminregistration')
    else:
        return render(request,'Admin/AdminRegistration.html',{"editadm":adm})

#Place Section
def Place(request):
    district=tbl_district.objects.all()
    Place=tbl_place.objects.all()
    if request.method=="POST":
        dist=tbl_district.objects.get(id=request.POST.get("sel_district"))
        place_name=request.POST.get("txt_place")
        tbl_place.objects.create(district=dist,place_name=place_name)
        return redirect('Admin:Place')
    else:
        return render(request,'Admin/Place.html',{"district":district,"place":Place})
    
def editPlace(request, eid):
    plac=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        plac.place_name=request.POST.get('txt_place')
        plac.save()
        return redirect('Admin:Place')
    else:
        return render(request,'Admin/Place.html',{"editPlace":plac})
    
def deletePlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect('Admin:Place')



#Subcategory
def Subcategory(request):
    category=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.all()
    if request.method=="POST":
        cat=tbl_category.objects.get(id=request.POST.get("sel_category"))
        subcategory_name=request.POST.get("txt_subcategory")
        tbl_subcategory.objects.create(category=cat,subcategory_name=subcategory_name)
        return render(request,'Admin/Subcategory.html')
    else:
        return render(request,'Admin/Subcategory.html',{"category":category,"subcategory":subcategory})
