from django.urls import path,include 
from User import views
app_name='User'
urlpatterns = [
    path('userDashboard/', views.userDashboard, name='userDashboard')
]
