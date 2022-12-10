from django.urls import path
from .views import profile , profile_edit , signup, myreservation, mylisting


app_name = 'accounts'

urlpatterns = [
    path('signup',signup , name='signup'),
    path('profile/',profile,name='profile'),
    path('reservation/', myreservation , name='reservation'),
    path('mylisting/', mylisting , name='mylisting'),
    path('profile/edit', profile_edit , name='profile_edit'),
]
