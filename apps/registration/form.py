from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from captcha.fields import CaptchaField

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label='First Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
        required=True,
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
        required=True,
    )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        widget=forms.TextInput(attrs={
            'autocorrect': 'off',
            'autocapitalize': 'none',
            'class': 'form-control',
            'placeholder': 'Enter Email'
        }),
        required=True,
    )
    password1 = forms.CharField(
        label='Password',
        max_length=100,
        widget=forms.TextInput(attrs={
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Enter Password'
        }),
        required=True,
    )
    password2 = forms.CharField(
        label='Repeat Password',
        max_length=100,
        widget=forms.TextInput(attrs={
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Enter Password Again'
        }),
        required=True,
    )
    captcha = CaptchaField()

    # Functions
    # ------------
    def clean_email(self):
        email = self.cleaned_data['email']
        if email != None and email != '':
            try:
                User.objects.get(email=email)
                raise forms.ValidationError("Email already exists.")
            except User.DoesNotExist:
                return email
        else:
            raise forms.ValidationError("Cannot be blank")

    def clean_is_18_or_plus(self):
        data = self.cleaned_data
        if data.get('is_18_or_plus'):
            return data
        else:
            raise forms.ValidationError("You must be 18 or over.")

    def clean_password_repeated(self):
        password = self.cleaned_data['password']  # cleaned_data dictionary has the
        # the valid fields
        password_repeated = self.cleaned_data['password_repeated']
        if password != password_repeated:
            raise forms.ValidationError("Passwords do not match.")
        return password_repeated

# Captcha Setup:
# http://django-simple-captcha.readthedocs.org/en/latest/usage.html#installation
