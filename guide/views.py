from django.shortcuts import render
from django.views import generic
from guide.models import Category, Guide

# Create your views here.
class IndexView(generic.ListView):
    model = Guide
    template_name = 'pages/index.html'
    context_object_name = 'guide_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()

        # And so on for more models
        return context
