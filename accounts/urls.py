from django.urls import path
from . import views

urlpatterns = [
    
     path('auth/login/',views.sign_in,name='login'),
     path('auth/signup/',views.SignUpView.as_view(),name='signup_view'),
     path('ajax/signup/',views.sign_up,name='signup'),
     path('auth/profile/',views.profile,name='profile')
 
]
