from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import UserProfile
from place.models import Category, Comment, Place, UserContentImageForm, Images
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import UserContentForm


# Create your views here.

def index(request):
	return HttpResponseRedirect("/user/profile")

@login_required(login_url='/login')
def profile(request):

	current_user=request.user
	profile= UserProfile.objects.get(user_id=current_user.id)
	categories=Category.objects.all()
	comments=Comment.objects.filter(user_id=current_user.id).order_by('-id')
	places=Place.objects.filter(user_id=current_user.id).order_by('-id')
	content={ 'profile':profile, 'categories':categories, 'comments':comments, 'places':places,}
	return render(request, 'profile.html',content)

@login_required(login_url='/login')
def profile_edit(request):

	if request.method=='POST':
		user_form=UserUpdateForm(request.POST, instance=request.user)
		profile_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request,"Profile Updated Successfully.")
			return HttpResponseRedirect('/user/profile')
		else:
			messages.warning(request,profile_form.errors)
			return HttpResponseRedirect('/user/profile_edit')
	else:
		categories=Category.objects.all()
		current_user=request.user
		user_form=UserUpdateForm(instance=request.user)
		profile_form=ProfileUpdateForm(instance=request.user.userprofile)
		profile=UserProfile.objects.get(user_id=current_user.id)
		content={'categories':categories, 'profile':profile, 'profile_form':profile_form }
		return render(request, 'profile_edit.html', content)


@login_required(login_url='/login')
def change_password(request):

	if request.method=='POST':
		form=PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user=form.save()
			update_session_auth_hash(request,user)
			messages.success(request,"Password changed successfully.")
			return HttpResponseRedirect('/user/change_password')
		else:
			messages.warning(request, "Please Correct the Error Below. <br>" + str(form.errors))
			return HttpResponseRedirect('/user/change_password')
	else:
		categories=Category.objects.all()
		form=PasswordChangeForm(request.user)
		content={'form':form, 'categories':categories}
		return render(request, 'password_change.html', content)


@login_required(login_url='/login')
def user_comments(request):

	categories=Category.objects.all()
	current_user=request.user
	comments=Comment.objects.filter(user_id=current_user.id)
	content={'categories':categories, 'comments':comments, }
	return render(request, 'profile.html', content)


@login_required(login_url='/login')
def deletecomment(request,id):

	current_user=request.user
	Comment.objects.filter(id=id, user_id=current_user.id).delete()
	messages.success(request, "Comment deleted successfully")
	return HttpResponseRedirect('/user/profile')


@login_required(login_url='/login')
def user_places(request):

	categories=Category.objects.all()
	current_user=request.user
	places=Place.objects.filter(user_id=current_user.id)
	content={'categories':categories, 'places':places, }
	return render(request, 'profile.html', content)



@login_required(login_url='/login')
def addcontent(request):

	form= UserContentForm(request.POST, request.FILES)
	if request.method=='POST':
		if form.is_valid():
			current_user=request.user
			data=Place()
			data.user_id=current_user.id
			data.category=form.cleaned_data['category']
			data.title=form.cleaned_data['title']
			data.keywords=form.cleaned_data['keywords']
			data.description=form.cleaned_data['description']
			data.image=form.cleaned_data['image']
			data.slug=form.cleaned_data['slug']
			data.detail=form.cleaned_data['detail']
			data.status='False'
			data.save()
			messages.success(request, "Your Place is Added Successfully.")
			return HttpResponseRedirect('/user/profile')
		else:
			messages.warning(request, "Please Correct the Error in Places Section. <br>" + str(form.errors))
			return HttpResponseRedirect('/user/addcontent')
	else:
		categories=Category.objects.all()
		content={'categories':categories, 'form':form,}
		return render(request, 'add-content.html', content)

@login_required(login_url='/login')
def editplace(request,id):
	
	place=Place.objects.get(id=id)
	if request.method=='POST':
		form=UserContentForm(request.POST, request.FILES, instance=place)
		if form.is_valid():
			form.save()
			messages.success(request, "Your Place is Updated Successfully.")
			return HttpResponseRedirect('/user/profile')
		else:
			messages.warning(request, "Please Correct the Error in Places Section. <br>" + str(form.errors))
			return HttpResponseRedirect('/user/editplace/'+str(id))
	else:
		categories=Category.objects.all()
		form=UserContentForm(instance=place)
		content={'categories':categories, 'form':form,}
		return render(request, 'add-content.html',content)


@login_required(login_url='/login')
def deleteplace(request,id):

	current_user=request.user
	Place.objects.filter(id=id, user_id=current_user.id).delete()
	messages.success(request, 'Place Deleted Successfully.')
	return HttpResponseRedirect('/user/profile')


def placeimage(request,id):
	if request.method=='POST':
		lasturl=request.META.get('HTTP_REFERER')
		form=UserContentImageForm(request.POST, request.FILES)
		if form.is_valid():
			data=Images()
			data.title=form.cleaned_data['title']
			data.place_id=id
			data.image=form.cleaned_data['image']
			data.save()
			messages.success(request, "Your image is added to the gallery.")
			return HttpResponseRedirect(lasturl)
		else:
			messages.warning(request, "Image Upload Error :" + str(form.errors))
			return HttpResponseRedirect(lasturl)
	else:

		places=Place.objects.get(id=id)
		images=Images.objects.filter(place_id=id)
		form=UserContentImageForm()
		content={'places':places, 'images':images,'form':form}
		return render(request, 'user_place_gallery.html', content)