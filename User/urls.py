from django.urls import path,include 
from User import views
app_name='User'
urlpatterns = [
    path('userDashboard/', views.userDashboard, name='userDashboard'),

    path('myProfile/', views.myProfile, name='myProfile'),
    path('editProfile/', views.editProfile, name='editProfile'),

    path('changePassword/', views.changePassword, name='changePassword'),

    path('feedback/', views.Feedback, name='feedback'),
    path('deleteFeedback/<int:did>', views.deleteFeedback, name='deleteFeedback'),
    
]
