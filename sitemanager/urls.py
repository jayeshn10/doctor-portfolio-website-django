from django.contrib import admin
from django.urls import path

from sitemanager import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.blogs, name='blogs'),
    path('single-blog/<slug:single_blog>/', views.singleblog, name='singleblog'),
    path('facilities/', views.facilities, name='facilities'),
    path('testimonials/', views.testimonial, name='testimonial'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('testurl/', views.testfunction, name='testurl'),

]
