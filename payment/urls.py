from django.urls import path

from . import views

app_name='payment'

urlpatterns = [
        path('charge/', views.charge, name='charge'),
        path( '', views.HomePageView.as_view(), name='home'),
]