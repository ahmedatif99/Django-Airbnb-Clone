from django.urls import path
from .views import PropertyDetail, PropertyList
from .api_view import PropertyAPIList, PropertyAPIDetails

app_name = 'property'

urlpatterns = [
    path('', PropertyList.as_view(), name='property_list'),
    path('<slug:slug>', PropertyDetail.as_view(), name='property_detail'),
    path('api/list', PropertyAPIList.as_view(), name='property_list_api'),
    path('api/list/<int:pk>', PropertyAPIDetails.as_view(), name='property_detail_api'),
]
