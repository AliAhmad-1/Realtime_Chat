from django.urls import path
from . import views
urlpatterns = [
    
    path('group_chat/<str:group_name>/',views.chat,name='chat'),
    path('person_chat/<str:username>/',views.person_chat,name='person_chat'),
    path('',views.home,name='home')
   
]
