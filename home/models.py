from django.db import models
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class UserProfile(models.Model):

	user=models.OneToOneField(User, on_delete=models.CASCADE)
	phone=models.CharField(blank=True, max_length=50)	
	city=models.CharField(blank=True, max_length=50)
	country=models.CharField(blank=True, max_length=50)
	image=models.ImageField(blank=True,upload_to='images/users/')

	def __str__(self):
		return self.user.username

	def user_name(self):
		return self.user.first_name + ' ' + self.user.last_name + '[' + self.user.username + ']'

	def image_tag(self):
		return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
	image_tag.short_description='Image'


class UserProfileForm(ModelForm):

	class Meta:
		model=UserProfile
		fields=['phone','city','country','image']

class ContactFormMessage(models.Model):

	STATUS=(

		('New', 'New'),
		('Read', 'Read'),
	)
	
	name=models.CharField(blank=True,max_length=50)
	email=models.CharField(blank=True,max_length=50)
	subject=models.CharField(blank=True,max_length=50)
	message=models.CharField(blank=True,max_length=255)
	status=models.CharField(max_length=10, choices=STATUS, default='New')
	ip= models.CharField(blank=True, max_length=20)
	note=models.CharField(blank=True, max_length=100)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class ContactForm(ModelForm):

	class Meta:
		model=ContactFormMessage
		fields=['name','email','subject','message', 'ip']




class Faq(models.Model):

	STATUS=(

		('True','Active'),
		('False', 'Inactive'),
	)

	orderNo=models.IntegerField()
	question=models.CharField(max_length=255)
	answer=models.TextField()
	status=models.CharField(max_length=10, choices=STATUS)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.question

class Setting(models.Model):

	STATUS=(

		('True','Active'),
		('False','Inactive'),
	)

	title=models.CharField(max_length=150)
	keywords=models.CharField(max_length=255)
	description=models.CharField(max_length=255)
	company=models.CharField(max_length=50)
	address=models.CharField(max_length=255)
	phone=models.CharField(max_length=25)
	fax=models.CharField(max_length=25)
	email=models.CharField(max_length=50)
	icon=models.ImageField(blank=True, upload_to='images/')
	facebook=models.CharField(max_length=50)
	instagram=models.CharField(max_length=50)
	twitter=models.CharField(max_length=50)
	aboutus=RichTextUploadingField()
	contact=RichTextUploadingField()
	status=models.CharField(max_length=10, choices=STATUS)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

