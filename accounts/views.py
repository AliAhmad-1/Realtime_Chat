from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm,UpdateProfileForm
from .models import MyUser
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def sign_in(request):
    if not request.user.is_authenticated:
        
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)

            if form.is_valid():
            
                username=form.cleaned_data['username']
                password=form.cleaned_data.get('password')
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('profile')

        else:
            form=AuthenticationForm()

    else:
        return redirect('home')
    

    return render(request,'app/login.html',{'form':form})


class SignUpView(TemplateView):
    template_name='app/signup.html'
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["form"] = SignUpForm()
        return context
    

def sign_up(request):

    if request.method=="POST":
        form=SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status':'OK'})
        else:
            return JsonResponse({'status':'Error','errors':form.errors})
    else:
        return JsonResponse({'status':'Error'})
       

@login_required()
def profile(request):
    if request.method =='POST':
        form=UpdateProfileForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UpdateProfileForm(instance=request.user)
    return render(request,'app/profile.html',{'form':form})