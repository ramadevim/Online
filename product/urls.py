from django.urls import path
from product import views

app_name='product'

urlpatterns = [
    path('',views.products_list,name='list'),
    path('<int:pk>/<str:slug>/',views.product_detail,name="product_detail")

]

