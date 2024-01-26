from django.urls import path
from . import views


urlpatterns =[

    path('', views.bookListView.as_view(), name = 'book_list'),
    # path('')

]