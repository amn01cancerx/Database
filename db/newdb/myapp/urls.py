from django.contrib import admin
from django.urls import path, include
from .views import *
from myapp import views

urlpatterns = [
    path('', MyApi.as_view(), name="MyApi"),
    path('lab_details', LabApi.as_view(), name="LabApi"),
    path('buy_medicine', BuyMedicine.as_view(), name="BuyMedApi"),
    path('book_apt', BookApt.as_view(), name="BookApt"),
    path('miss_lab', MissLab.as_view(), name= "MissLab"),
    path('miss_med', MissMed.as_view(), name="MissMed"),
    path('cia', CheckIntoArray.as_view(), name="cia")
    
]