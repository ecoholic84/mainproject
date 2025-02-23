from django.shortcuts import render, redirect
from Guest.models import *
from User.models import *

# Create your views here.
def userDashboard(request):
    return render(request,'User/userDashboard.html')

def myProfile(request):
    thisProfile=tbl_user.objects.get(id=request.session['u_id'])
    return render(request,'User/myProfile.html', {'thisProfile':thisProfile})

def editProfile(request):
    editProfile=tbl_user.objects.get(id=request.session['u_id'])
    if request.method=="POST":
        editProfile.user_name=request.POST.get('txt_name')
        editProfile.user_email=request.POST.get('txt_email')
        editProfile.user_contact=request.POST.get('txt_contact')
        editProfile.user_address=request.POST.get('txt_address')
        editProfile.save()
        return redirect('User:myProfile')
    else:
        return render(request, 'User/editProfile.html', {'editProfile':editProfile})

def changePassword(request):
    loggedUser=tbl_user.objects.get(id=request.session['u_id'])
    if request.method=="POST":
        oldPassword=request.POST.get('txt_old_password')
        newPassword=request.POST.get('txt_new_password')
        confirmPassword=request.POST.get('txt_confirm_password')
        if loggedUser.user_password==oldPassword:
            if newPassword==confirmPassword:
                loggedUser.user_password=newPassword
                loggedUser.save()
            else:
                return redirect('User:myProfile')
        else:
            return redirect('User:myProfile')
    return render(request, 'User/changePassword.html')

# Feedback
def Feedback(request):
    fb=tbl_feedback.objects.all()
    if request.method=="POST":
        content=request.POST.get("txt_feedback")
        tbl_feedback.objects.create(feedback_content=content,user_id=tbl_user.objects.get(id=request.session['u_id']))
        return redirect('User:feedback')
    else:
        return render(request,'User/feedback.html',{'feed':fb})
        
def deleteFeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect('User:feedback')