from django.contrib import admin
from place.models import District, Place, Images, Comment
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from django.utils.html import format_html
# Register your models here.


############################################################################################

#ADMIN FIELDS WHICH ARE CREATED IN MODELS ARE DEFINED HERE

############################################################################################

class PlaceImageInline(admin.TabularInline):
	model= Images
	extra= 5


class DistrictAdmin(admin.ModelAdmin):

	list_display=['title', 'status','parent','image_tag']
	list_filter=['status','created_at']
	readonly_fields=('image_tag',)

class PlaceAdmin(admin.ModelAdmin):

	list_display=['title','district','image_tag','status']
	list_filter=['status','created_at','district']
	inlines=[PlaceImageInline]
	readonly_fields=('image_tag',)
	prepopulated_fields={'slug':('title',)}

class ImageAdmin(admin.ModelAdmin):
	list_display=['title', 'place', 'image_tag']
	readonly_fields=('image_tag',)


class DistrictAdmin2(DraggableMPTTAdmin):
	
	mptt_indent_field="title"
	list_display=('tree_actions', 'indented_title', 'related_places_count', 
		'related_places_cumulative_count')
	list_display_links=('indented_title',)
	prepopulated_fields={'slug':('title',)}

	def get_queryset(self, request):
		qs= super().get_queryset(request)

		qs=District.objects.add_related_count(
			qs,
			Place,
			'district',
			'places_cumulative_count',
			cumulative=True)

		qs=District.objects.add_related_count(
			qs,
			Place,
			'district',
			'places_count',
			cumulative=False)

		return qs

	def related_places_count(self, instance):
		return instance.places_count
	related_places_count.short_description='Related Places (For This District)'

	def related_places_cumulative_count(self, instance):
		return instance.places_cumulative_count
	related_places_cumulative_count.short_description='Related Places(In Tree)'


class CommentAdmin(admin.ModelAdmin):
	list_display=['subject','place', 'user', 'status', 'created_at']
	list_filter=['status', 'created_at']
	list_editable=['status']

admin.site.register(District, DistrictAdmin2)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Images, ImageAdmin)
admin.site.register(Comment,CommentAdmin)