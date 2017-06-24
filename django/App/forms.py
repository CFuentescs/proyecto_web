from django import forms

class LoginForm (forms-form):
    username=forms.CharField()
    password=form-CharField(widget=forms.PasswordInput())