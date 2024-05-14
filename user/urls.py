from django.urls import path
from . import views
####################################################################

#PLACE APPLICATION URLS

####################################################################

urlpatterns=[

	# ex: /user/
	path('',views.index,name="index"),
	# ex:/user/profile
	path('profile', views.profile, name="profile"),
	# ex:/user/profile_edit
	path('profile_edit', views.profile_edit, name="profile_edit"),
	# ex:/user/change_password
	path('change_password', views.change_password, name="change_password"),
	# ex:/user/deletecomment/1
	path('deletecomment/<int:id>', views.deletecomment, name="deletecomment"),
	# ex:/user/addcontent
	path('addcontent', views.addcontent, name="addcontent"),
	# ex:/user/editplace/1
	path('editplace/<int:id>', views.editplace, name="editplace"),
	#ex: /user/deleteplace/1
	path('deleteplace/<int:id>', views.deleteplace, name="deleteplace"),
	#ex: /user/placeimage/1
	path('placeimage/<int:id>', views.placeimage, name="placeimage"),

]