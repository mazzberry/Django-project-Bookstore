from django import forms
from .models import books, comments
class BooksForm(forms.ModelForm):
    class Meta:
        model = books
        fields = [
            'title',
            'author',
            'description',
            'price',
            'book_cover',
        ]

class CommentsForm(forms.ModelForm):

    class Meta:
        model = comments
        fields = ('text','recommend',)