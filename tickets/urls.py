from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('tickets/', views.tickets, name='tickets'),
    path('tickets/details/<int:id>', views.details, name='details'),
]