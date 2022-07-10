import datetime
import re

from django import forms
from django.contrib.auth.models import User


def email_validator(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, email)


class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 2:
            raise forms.ValidationError("Username must be at least 2 characters")
        elif len(username) > 30:
            raise forms.ValidationError("Username must be less than 30 characters")
        elif User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username {} already exists".format(username))

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email_validator(email):
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email you entered already exists")
        else:
            raise forms.ValidationError("Please enter a valid email")

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 3:
            raise forms.ValidationError("Password must be at least 3 characters")
        elif len(password1) > 25:
            raise forms.ValidationError("Password must be less than 25 characters")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Please make sure both passwords matched")

        return password2


class SigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username doesn't exist")

        return username


class SearchForm(forms.Form):
    CHOICES = ()
    for i in range(11):
        CHOICES += ((i + 1, str(i + 1)),)
    CHOICES += ((12, '12+'),)

    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    hour = forms.TimeField(
        widget=forms.TimeInput(attrs=dict(type='time', value="08:00", min="08:00", max="24:00", step="1800")))
    hc = forms.ChoiceField(choices=CHOICES)

    def clean_date(self):
        date = self.cleaned_data['date']
        # Check date is not in the past.
        if date < datetime.date.today():
            raise forms.ValidationError("Invalid date")

        return date
