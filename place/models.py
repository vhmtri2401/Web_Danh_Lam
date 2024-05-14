from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from mptt.fields import TreeForeignKey
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.


###########################################################################################

#PLACES DATABASE TABLE

###########################################################################################

class Category(MPTTModel):

	STATUS=(

		('True','Active'),
		('False','Inactive'),
	)
	title= models.CharField(max_length=100)
	keywords=models.CharField(max_length=255)
	description=models.CharField(max_length=255)
	image=models.ImageField(blank=True,upload_to='images/')
	status=models.CharField(max_length=10, choices=STATUS)
	slug=models.SlugField(null=False, unique=True)
	parent=TreeForeignKey('self',blank=True,null=True,related_name='children', on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	
	class MPTTMeta:
		order_insertion_by=['title']			

	def __str__(self):
		full_path=[self.title]
		k=self.parent
		while k is not None:
			full_path.append(k.title)
			k=k.parent
		return '->'.join(full_path[::-1])

	def image_tag(self):
		return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
	image_tag.short_description='Image'



class Place(models.Model):

	STATUS=(

		('True', 'Active'),
		('False', 'Inactive')
	)
	user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	category=models.ForeignKey(Category, on_delete=models.CASCADE) #Relationship with Category Table
	title=models.CharField(max_length=150)
	keywords=models.CharField(max_length=255)
	description=models.CharField(max_length=255)
	image=models.ImageField(blank=True, upload_to='images/')
	detail=RichTextUploadingField()
	slug=models.SlugField(null=False, unique=True)
	status=models.CharField(max_length=25,choices=STATUS)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def image_tag(self):
		return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
	image_tag.short_description='Image'


class Images(models.Model):
	place=models.ForeignKey(Place,on_delete=models.CASCADE)
	title=models.CharField(max_length=50,blank=True)
	image=models.ImageField(blank=True, upload_to='images/')

	def __str__(self):
		return self.title

	def image_tag(self):
		return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
	image_tag.short_description='Image'


class Comment(models.Model):
	STATUS= (

		('New', 'New'),
		('True', 'Active'),
		('False', 'Inactive'),
	)
	place=models.ForeignKey(Place, on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	subject=models.CharField(max_length=50)
	comment=models.CharField(max_length=255)
	rate=models.CharField(max_length=10)
	ip=models.CharField(max_length=20)
	status=models.CharField(max_length=10, choices=STATUS, default='New')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.subject

class CommentForm(ModelForm):

	class Meta:
		model= Comment
		fields=['subject', 'rate', 'comment']


def get_absolute_url(self):
	return reverse('category_detail', kwargs={'slug': self.slug})


class UserContentImageForm(ModelForm):
	class Meta:
		model=Images
		fields=['title', 'image']