from django.shortcuts import render
from django.views.generic import ListView
from .models import Tag

# Create your views here.
class TagListView(ListView):
    template_name = 'tags/tag_list.html'
    queryset = Tag.objects.all()