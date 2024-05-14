from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from home.models import UserProfile
from django.forms import FileInput
from place.models import Place
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm




class UserUpdateForm(UserChangeForm):

	class Meta:
		model=User
		fields=('username', 'email', 'first_name', 'last_name',)

class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model=UserProfile
		fields=('phone', 'city', 'country', 'image',)
		

class UserContentForm(ModelForm):

	class Meta:
		model= Place
		fields=['category', 'title',  'slug', 'keywords', 'description', 'image', 'detail']
		widgets={

			'title': forms.TextInput(attrs={'class':'input'}),
			'slug': forms.TextInput(attrs={'class':'input'}),
			'keywords': forms.TextInput(attrs={'class':'input'}),
			'description': forms.TextInput(attrs={'class':'input'}),
			'image': forms.FileInput(attrs={'class':'input'}),
			'detail':CKEditorWidget(),
		}