from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from place.models import Comment, CommentForm,Place, Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
import json

# Create your views here.

#################################################################################

#PLACE APPLICATION VIEWS

#################################################################################

def index(request):
	
	return None

@login_required(login_url='/login')
def placeComment(request,id):

	url=request.META.get('HTTP_REFERER')
	#return HttpResponseRedirect(url)
	if request.method== 'POST':
		form=CommentForm(request.POST)
		if form.is_valid():
			current_user=request.user
			data=Comment()
			data.user_id=current_user.id
			data.place_id=id
			data.subject=form.cleaned_data['subject']
			data.comment=form.cleaned_data['comment']
			data.rate=form.cleaned_data['rate']
			data.ip=request.META.get('REMOTE_ADDR')
			data.save()
			messages.success(request, "Thanks For Your Comment! Your Comment Will Be Shown After Approved.")
			return HttpResponseRedirect(url)

	messages.warning(request, "Your Comment Could Not Been Sent. Please Check Your Comment.")
	return HttpResponseRedirect(url)

def search(request):

	if request.method== 'POST':
		form=SearchForm(request.POST)
		if form.is_valid():
			category=Category.objects.all()
			categories=Category.objects.all()
			query=form.cleaned_data['search']
			results=Place.objects.filter(title__icontains=query)
			content={'results':results,'categories':categories}
			return render(request, 'place-search.html', content)
	return HttpResponseRedirect('/')


def search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    places = Place.objects.filter(title__icontains=q)
    results = []
    for pl in places:
      place_json = {}
      place_json = pl.city + "," + pl.state
      results.append(place_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)