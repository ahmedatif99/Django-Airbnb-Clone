from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
from .models import Property, Place,  PropertyBook, Category, PropertyImages, PropertyReview

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

    
admin.site.register(Property,SomeModelAdmin)
admin.site.register(PropertyBook)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Place)
admin.site.register(Category)

