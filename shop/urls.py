from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
#from cart.views import cart_details

urlpatterns = [
    path('', views.home, name='hm'),
    path('<slug:c_slug>/', views.home, name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>', views.prodDetails, name='details'),
    path('search', views.searching, name='search'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('cart/', views.cart_details, name='cart')


]

