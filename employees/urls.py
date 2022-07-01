from django.urls import path

from .import views

urlpatterns=[
    path('emplooyes',views.login),
    path('home',views.home),
]