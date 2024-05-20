from django import forms 
from blogs.models import BlogPost
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
INPUT_DES = 'px-5 py-3 rounded-xl border'


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'enter title',
                'class': 'w-1/2 my-3 py-4 px-6 rounded-xl border'
            }),
            'content': forms.TextInput(attrs={
                'placeholder': 'enter content',
                'class': 'w-1/2 my-3 py-4 px-6 rounded-xl border'
            }),
            'publication_date': forms.DateInput(attrs={
                # 'placeholder': 'enter password',
                'class': 'w-1/2 my-3 px-5 py-3 rounded-xl border'
            }),
            'author': forms.Select(attrs={
                # 'placeholder': 'enter password',
                'class': 'w-1/2 my-3 px-5 py-3 rounded-xl border'
            }),
            
            }
        
        
        



class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ('username','password')
        widgets = {
            'usernam':forms.TextInput(attrs={
                'placholder':'enter username',
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'password':forms.PasswordInput(attrs={
                'placeholder':'enter password',
                'class':'px-5 py-3 rounded-xl border'
            }),
        }
        
        
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'enter username',
                'class': 'w-1/2 py-4 px-6 rounded-xl border'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'enter email',
                'class': 'w-1/2 py-4 px-6 rounded-xl border'
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'enter password',
                'class': 'w-1/2 px-5 py-3 rounded-xl border'
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'enter password',
                'class': 'w-1/2 px-5 py-3 rounded-xl border'
            })}
        
        