from django.contrib import admin

# Register your models here.
from .models import Property, Place,  PropertyBook, Category, PropertyImages, PropertyReview

admin.site.register(Property)
admin.site.register(PropertyBook)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Place)
admin.site.register(Category)