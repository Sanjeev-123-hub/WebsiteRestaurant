from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('menu.html/', views.menu, name='menu'),
    path('admin.html/', views.admin , name='admin'),
    path('contact.html/', views.contact, name='contact'),
    path('report.html/', views.report, name='report'),
]