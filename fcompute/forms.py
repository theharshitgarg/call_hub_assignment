from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField()
    password1 = forms.EmailField()


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, widget=forms.TextInput)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)
