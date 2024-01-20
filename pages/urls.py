from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('contactus/', views.contactusPageView.as_view(), name = 'contactus'),
    # path('about-us/', views.aboutUsview.as_view(), name = 'about-us')
]