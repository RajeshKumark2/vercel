from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('blog', views.blog,name='blog'),
    path('resume', views.resume,name='resume'),
    path('skils', views.skils,name='skils'),
]

