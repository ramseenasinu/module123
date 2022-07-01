from django.urls import path

app_name='jadmin'
from . import views
urlpatterns=[
    path('home',views.homes,name="homes"),
    path('login',views.loges,name="loges"),

]