"""onlineshopp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from shop import views
from django.contrib.auth import views as auth_views

from django.contrib.auth import settings
from django.conf.urls.static import static
# from cart.views import cart_view

from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='shop/logout.html'), name='logout'),
      path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='shop/pwreset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='shop/pwresetdone.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='shop/pwresetconfirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='shop/pwresetcomplete.html'
         ),
         name='password_reset_complete'),

    path('register/',views.register,name='register'),
    path('profile/', views.profile,name='profile'),
    path('hello/', views.testhome,name='testhome'),
    path('',include('product.urls',namespace='products')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('search/',include('search.urls',namespace='search')),
    path('order/', include('orders.urls', namespace='order')),
    path('pdf/',views.some_view,name='pdf'),
# path('checkout/', include('checkout.urls',namespace='checkout')),

    path('payment/', include('payment.urls',namespace='payment')),
    path('bootstrap/',TemplateView.as_view(template_name='bootstrap/example.html')),
    # path('',include('search.urls',namespace='searching'))


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


