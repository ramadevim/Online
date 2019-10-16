
from django import forms
from .models import Contact,Register,Login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Profile

class Contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
    message=forms.CharField(max_length=100,widget=forms.Textarea)

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if not 'gmail.com' in email:
            raise forms.ValidationError('not match')
        return email


class Registrationform(forms.ModelForm):
    class Meta:
        model=Register
        fields='__all__'

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'
    password = forms.CharField(widget=forms.PasswordInput)


class UserupdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileupdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

# class UserProfileInfoForm(forms.ModelForm):
#         class Meta():
#             model = UserProfileInfo
#             fields = ('portfolio_site', 'profile_pic')



    # password=forms.CharField(label="password",max_length=100,widget=forms.PasswordInput)
    # c_password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    # class Meta():
    #     model = Reg
    #     fields = ('username','email','password')
