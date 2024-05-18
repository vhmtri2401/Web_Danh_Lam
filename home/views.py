from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Setting, ContactFormMessage, ContactForm, Faq, UserProfile
from place.models import Place, District, Images, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from .forms import SignUpForm

# Create your views here.

################################################################################

#HOME APPLICATION VIEWS

################################################################################

def index(request):

	setting= Setting.objects.get(pk=1)
	slider= Place.objects.filter(status='True').order_by('?')[:3]
	districts=District.objects.all()
	checkOutPlaces=Place.objects.filter(status='True')[:10]
	bestPlaces=Place.objects.filter(status='True').order_by('-id')[:4]

	content= {'setting': setting, 'page': 'home', 'slider':slider, 'districts':districts,
				'checkOutPlaces':checkOutPlaces, 'bestPlaces': bestPlaces }
	return render(request, 'index.html', content)

def about(request):

	about= Setting.objects.get(pk=1)
	districts=District.objects.all()
	content= {'about': about, 'page':'about', 'districts':districts }
	return render(request, 'about.html', content)

def contact(request):


	if request.method== 'POST':

		form=ContactForm(request.POST)
		if form.is_valid():
			data=ContactFormMessage() #model connection
			data.name= form.cleaned_data['name']
			data.email= form.cleaned_data['email']
			data.subject= form.cleaned_data['subject']
			data.message= form.cleaned_data['message']
			data.ip= request.META.get('REMOTE_ADDR')
			messages.success(request, "Your message has been sent. Thank you!")
			data.save()
			return HttpResponseRedirect('/contact')

	contact=Setting.objects.get(pk=1)
	districts=District.objects.all()
	content={'contact':contact, 'page':'contact', 'districts':districts}
	return render(request, 'contact.html', content)


def place(request):

	districts=District.objects.all()
	places=Place.objects.filter(status='True')
	content={'districts' : districts, 'places':places}
	return render(request, 'place.html', content)


def placeDetail(request,id,slug):

	try:
		districts=District.objects.all()
		place=Place.objects.get(id=id)
		gallery= Images.objects.filter(place_id=id)
		district=District.objects.all()
		lastPlaces=Place.objects.filter(status='True').order_by('-id')[:3]
		comments= Comment.objects.filter(place_id=id,status='True')
		content={'place':place, 'gallery':gallery, 'district':district, 'lastPlaces':lastPlaces,
		 'comments':comments, 'districts':districts}
		return render(request, 'place-detail.html', content)
	except:
		return HttpResponseRedirect('/error')

def logout_view(request):

	logout(request)
	return HttpResponseRedirect('/')

def login_view(request):

	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect('/')
		else:
			messages.warning(request, "Please check your username or password.")
			return HttpResponseRedirect('/login')
	districts=District.objects.all()
	content={'districts':districts}
	return render(request, 'login.html',content)


def signup_view(request):

	if request.method=='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password1')
			user=authenticate(request,username=username, password=password)
			login(request,user)
			current_user=request.user
			data=UserProfile()
			data.user_id=current_user.id
			data.image="images/users/user.jpg"
			data.save()
			return HttpResponseRedirect('/')
		else:
			messages.warning(request,form.errors)
			return HttpResponseRedirect('/login/')
	districts=District.objects.all()
	content={'districts':districts}
	return render(request, 'login.html',content)

def error(request):
	districts=District.objects.all()
	content={'districts':districts}
	return render(request, '404.html',content)



def faq(request):
	districts=District.objects.all()
	faqs=Faq.objects.all().order_by('orderNo')
	content={'districts':districts, 'faqs':faqs}
	return render(request, 'faq.html',content)