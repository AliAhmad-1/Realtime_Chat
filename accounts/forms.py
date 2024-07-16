from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from .models import MyUser
from django import forms

class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=200,required=True)
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(render_value=True))
    password2=forms.CharField(label='Password confirmation',widget=forms.PasswordInput(render_value=True))

    class Meta:
        model=MyUser
        fields=['username','password1','password2']

       
class UpdateProfileForm(UserChangeForm):
    password=None
    
    username=forms.CharField(max_length=150)
    email=forms.EmailField(required=False,widget=forms.EmailInput(attrs={'placeholder':'test@gmail.com'}))
    class Meta:
        model=MyUser
        fields=['photo','username','email']
        
