from django.contrib import admin
from home.models import Setting, ContactFormMessage, UserProfile, Faq

# Register your models here.

##############################################################################################

#REGISTER MODELS WHICH ARE CREATED IN MODELS.PY

##############################################################################################

class ContactFormAdmin(admin.ModelAdmin):

	list_display=['name','subject','status', 'created_at']
	list_filter=['status','created_at']


class UserProfileAdmin(admin.ModelAdmin):

	list_display=['user_name','phone','city', 'country' ]


class FaqAdmin(admin.ModelAdmin):

	list_display=['orderNo','question', 'status','created_at' ]
	list_filter=['status', 'created_at']
	list_editable=['status']

admin.site.register(ContactFormMessage,ContactFormAdmin)
admin.site.register(Setting)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Faq,FaqAdmin)