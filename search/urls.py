from django.urls import path
from .views import searchview
app_name='search'

urlpatterns = [
    path('',searchview.as_view(),name='query'),
]