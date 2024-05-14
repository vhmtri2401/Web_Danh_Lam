from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

	username=forms.CharField(max_length=30)
	email=forms.EmailField(max_length=200)
	first_name=forms.CharField(max_length=50)
	last_name=forms.CharField(max_length=50)

	class Meta:
		model= User
		fields=('username','email', 'password1','first_name','last_name','password2')