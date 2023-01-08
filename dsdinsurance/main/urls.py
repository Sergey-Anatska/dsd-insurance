from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('calculator', views.calculator, name='calculator'),
    path('benefits', views.benefits, name='benefits'),
    path('partners', views.partners, name='partners'),
    path('feedback', views.feedback, name='feedback'),
    path('contact', views.partners, name='contact'),

]