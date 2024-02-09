from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import books
from .forms import BooksForm
# Create your views here.

class BookListView(generic.ListView):
    model = books
    paginate_by = 3 #paginate_by -> gives us a page with 4(e.x) object that exist in DB and next & previous
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(generic.DetailView):
    model = books
    template_name = 'books/book_detail.html'

class BookCreateView(generic.CreateView):
    # model = books  // agar model be createview bedim mitoonim **(FORM_CLASS RA BEHESH NADIM)* va khodesh form ro misaze
    # fields = ['title',
    #         'author',
    #         'description',
    #         'price',]

    form_class = BooksForm
    template_name = 'books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = books
    form_class = BooksForm
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = books
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')


