from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
from .models import Property, Place,  PropertyBook, Category, PropertyImages, PropertyReview

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name', 'price', 'get_avg_rating', 'check_availability']

    
admin.site.register(Property,SomeModelAdmin)

class PropertyBookAdmin(admin.ModelAdmin):
    list_display = ['property', 'in_progress']

admin.site.register(PropertyBook, PropertyBookAdmin)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Place)
admin.site.register(Category)

