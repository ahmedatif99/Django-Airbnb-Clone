from django.shortcuts import render, redirect
from django.views.generic.edit import FormMixin

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from .models import Property
from .forms import PropertyBookForm
from .filters import PropertyFilters
from django_filters.views import FilterView

class PropertyList(FilterView):
    model = Property
    paginate_by = 1
    filterset_class = PropertyFilters
    template_name = 'property/property_list.html'
    
    # filter
    # Pagenation

class PropertyDetail(FormMixin, DetailView):
    model= Property
    form_class = PropertyBookForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Property.objects.filter(category=self.get_object().category)[:2]
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()

            return redirect('/')
        
        # book

class AddListing(CreateView):
    pass