from django import forms
from django.contrib.auth.models import User
from user.models import Profile

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı Adı")
    first_name = forms.CharField(max_length=50,label="Ad")
    last_name = forms.CharField(max_length=50,label="Soyad")
    email = forms.EmailField(max_length=50,label="Mail Adresi")
    password = forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Parola Doğrula",widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")

        if User.objects.filter(username__iexact=username).exists():  
            raise forms.ValidationError('Bu kullanıcı adı kullanılıyor...')
        if password and confirm and (password != confirm): 
            raise forms.ValidationError("Parolalar Eşleşmiyor")  
        else:
            values = {
                "username" : username,
                "password" : password,
                "first_name": first_name,
                "last_name" : last_name,
                "email": email,
 
            }
            return values 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["age","city","phone","address"]

class LoginForm(forms.Form): # (216)
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget= forms.PasswordInput) 
    