from django.urls import path

from . import views
app_name='jseeker'
urlpatterns=[
    path('',views.login,name='log',),
    path('jobsearch',views.search,name='search'),
    path('jobdeatails',views.deatail,name='details'),
]