from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('check-in/', views.Check_In, name="check-in"),
    path('check-out/', views.Check_Out, name="check-out"),
    path('add-user/', views.AddUser, name="add-user"),

]