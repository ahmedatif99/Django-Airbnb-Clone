from django.shortcuts import render
from django.db.models.query_utils import Q
from django.db.models import Count
from django.contrib.auth.models import User

from property.models import Property, Place, Category
from blog.models import Post

# Create your views here.



def home(request):
    places = Place.objects.all().annotate(property_count = Count('property_place'))
    category = Category.objects.all()

    resturant_list = Property.objects.filter(category__name='Resturant')[:5]
    hotels_list = Property.objects.filter(category__name='Hotels')[:4]
    places_list = Property.objects.filter(category__name='Places')[:4]

    recent_posts = Post.objects.all()[:4]

    users_count = User.objects.all().count()
    places_count = Property.objects.filter(category__name='Places').count()
    resturant_count = Property.objects.filter(category__name='Resturant').count()
    hotels_count = Property.objects.filter(category__name='Hotels').count()

    return render(request,'settings/home.html',{
        'places': places,
        'category': category,
        'resturant_list': resturant_list,
        'hotels_list': hotels_list,
        'places_list': places_list,
        'recent_posts': recent_posts,
        'users_count': users_count,
        'places_count': places_count,
        'resturant_count': resturant_count,
        'hotels_count': hotels_count,
    })

def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')

    property_list = Property.objects.filter(
            Q(name__icontains=name) &
            Q(place__name__icontains=place)
        )
    return render(request, 'settings/home_serach.html', {'property_list':property_list})

def category_filter(request, category):
    category = Category.objects.get(name=category)

    property_list = Property.objects.filter(
        category=category
    )
    return render(request, 'settings/home_serach.html', {'property_list':property_list})

def contact_us(request):
    pass