from django.shortcuts import render
from django.views import generic
from .models import books
# Create your views here.

class bookListView(generic.ListView):
    model = books
    template_name = 'books/book_list.html'
    context_object_name = 'books'