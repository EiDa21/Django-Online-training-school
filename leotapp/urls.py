from django.urls import path
from . import views

app_name = "leotapp"

urlpatterns =[
    path('', views.home, name ='home'),
    path('phonereg/', views.phonereg, name ='phonereg'),
]