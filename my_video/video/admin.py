from django.contrib import admin
from . import models

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	fields = ['mobile','fname','lname']

	search_fields=['mobile','fname','lname']

class MovieAdmin(admin.ModelAdmin):


	search_fields=['title']	

	list_filter=['year']

	list_display=['title','year']

	list_editable=['year']

admin.site.register(models.Movie,MovieAdmin)
admin.site.register(models.Customer,CustomerAdmin)