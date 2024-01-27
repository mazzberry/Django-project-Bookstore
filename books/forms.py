from django import forms
from .models import books
class BooksForm(forms.ModelForm):
    class Meta:
        model = books
        fields = [
            'title',
            'author',
            'description',
            'price',
        ]