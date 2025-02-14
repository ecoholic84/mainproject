from django.urls import path,include 
from Admin import views
app_name='Admin'
urlpatterns = [
    path('district/',views.district,name='district'),
    path('deletedistrict/<int:did>',views.deletedistrict,name='deletedistrict'),
    path('editdistrict/<int:eid>',views.editdistrict,name='editdistrict'),
    path('category/',views.category,name='category'),
    path('deletecategory/<int:did>',views.deletecategory,name='deletecategory'),
    path('editcategory/<int:eid>',views.editcategory,name='editcategory'),
    path('adminregistration/',views.AdminRegistration,name='adminregistration'),
    path('deleteadmin/<int:did>',views.deleteadmin,name='deleteadmin'),
    path('editadmin/<int:eid>',views.editadmin,name='editadmin'),
    path('place/',views.Place,name="Place"),
    path('deletePlace/<int:did>',views.deletePlace,name="deletePlace"),
    path('editPlace/<int:eid>',views.editPlace,name='editPlace'),  
    path('subcategory/',views.Subcategory,name="Subcategory"),
]
