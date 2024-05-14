
#####################################################

#HOME APPLICATION URLS


######################################################

from django.urls import path

from . import views

urlpatterns=[
	
	# ex: /home/
	path('',views.index,name="index"),
	# ex: /about/
	path('about', views.about, name="about"),
	# ex: /contact/
	path('contact', views.contact, name="contact"),
	# ex:/place/
	path('place', views.place, name="place"),
	# ex:/place/1/statue
	path('place/<int:id>/<slug:slug>', views.placeDetail, name="placeDetail"),
	# ex:/error/
	path('error', views.error, name="error"),
	# ex:/faq/
	path('faq',views.faq, name="faq"),
]