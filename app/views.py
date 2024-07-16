from django.shortcuts import render,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q


            
@login_required          
def home(request):
    users=MyUser.objects.all().exclude(username=request.user.username)
    if request.method=='POST':
            group_name=request.POST.get('group_name')
            group=Group.objects.filter(group_name=group_name)
            if group:
                return redirect('chat',group_name)
    
    return render(request,'app/home.html',{'users':users})

@login_required
def chat(request,group_name):
    group=Group.objects.filter(group_name=group_name).first()

    chats=[]
    if group:
        chats=Chat.objects.filter(group=group)
    else:
        group=Group(group_name=group_name)
        group.save()

    return render(request,'app/chat_group.html',{'group_name':group_name,'chats':chats})


@login_required
def person_chat(request,username):
    other_user=get_object_or_404(MyUser,username=username)
    if (request.user.id > other_user.id):
        thread_name=f'chat_{request.user.id}-{other_user.id}'
    else:
        thread_name=f'chat_{other_user.id}-{request.user.id}'
    chats=Chat.objects.filter(thread_name=thread_name)
    all_notifi=Notification.objects.filter(is_seen=False,owner=request.user)
    for i in all_notifi:
        i.is_seen=True
        i.save()
       
    return render(request,'app/person_chat.html',{'other_user':other_user,'chats':chats})

