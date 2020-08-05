from django.urls import path
from myapp import views
app_name = "myapp"


urlpatterns = [
   path('trail/',views.trail,name='trail'),
    path('profile/',views.profile,name='profile'),
     path('',views.home,name="home"),
     path('base/',views.base,name="base"),
    
]

