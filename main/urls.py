from django.urls import path 
from main import views 


urlpatterns = [
    path('userhome/',views.userhome,name="userhome"),
    path('adminhome/',views.adminhome,name='adminhome'),
    
]