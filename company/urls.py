from django.urls import path
from . import views

urlpatterns=[
    path('update-company/', views.update_company, name='update-company'),
    path('company-details/', views.company_details, name='company-details'),
]