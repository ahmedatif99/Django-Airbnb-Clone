from django.shortcuts import render, redirect
from django.views.generic.edit import FormMixin

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from .models import Property
from .forms import PropertyBookForm, PropertyImageFormeSet,PropertyForm
from .filters import PropertyFilters
from django_filters.views import FilterView
from django.urls import reverse
from django.contrib import messages

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
    success_url = '/property/'


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
    model = Property
    # form_class = PropertyForm
    fields = ['name','description','price','place','image', 'category']

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        image_formset = PropertyImageFormeSet

        return self.render_to_response(self.get_context_data(
            form = form,
            imageformset = image_formset
        ))


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        image_formsets = PropertyImageFormeSet(self.request.POST, self.request.FILES)

        if form.is_valid() and image_formsets.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            property = Property.objects.get(id=myform.id)
            for form in image_formsets:
                myform2 = form.save(commit=False)
                myform2.property = property
                myform2.save()

            messages.success(request, 'Successfully Added Your Property')

            return redirect(reverse('property:property_list'))