from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput

from apps.account.models import PrivateMessage


class PrivateMessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMessage
        fields = ['from_address', 'title', 'text']
        labels = {
            'from_address': 'From',
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': TextInput(
                attrs={'class': u'form-control', 'placeholder': u'Enter First Name', 'required': True}),
            'last_name': TextInput(
                attrs={'class': u'form-control', 'placeholder': u'Enter Last Name', 'required': True}),
            'email': TextInput(attrs={'class': u'form-control', 'placeholder': u'Enter Email', 'required': True}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name != None and first_name != '':
            return first_name
        else:
            raise forms.ValidationError("Cannot be blank")

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name != None and last_name != '':
            return last_name
        else:
            raise forms.ValidationError("Cannot be blank")

    def clean_email(self):
        email = self.cleaned_data['email']
        if email != None and email != '':
            return email
        else:
            raise forms.ValidationError("Cannot be blank")

    def clean(self):
        cleaned_data = super(UserForm, self).clean()

        # Verify no duplicate emails occur.
        try:
            email = cleaned_data.get("email")
            user = User.objects.get(email=email)
            if user != self.instance:
                raise forms.ValidationError("Email already exists")
        except User.DoesNotExist:
            pass
