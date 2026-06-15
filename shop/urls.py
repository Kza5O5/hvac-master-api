from django.urls import path
from . import views
from .views import * 
from django.conf import settings
from django.conf.urls.static import static
from .health_views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
        path(
    'auth/register/',
    RegisterView.as_view(),
    name='register'
),

path(
    'auth/login/',
    TokenObtainPairView.as_view(),
    name='login'
),

path(
    'auth/token/refresh/',
    TokenRefreshView.as_view(),
    name='token_refresh'
),

path(
    'profile/',
    ProfileView.as_view(),
    name='profile'
),

path(
    'change-password/',
    ChangePasswordView.as_view(),
    name='change_password'
),

path(
    'Service/',
    ServiceListCreate.as_view(),
    name='ServiceList'
),

path(
    'Service/<int:pk>/',
    ServiceDetail.as_view(),
    name='ServiceDetail'
),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/blog_details/<int:pk>/', views.blog_details, name='blog_details'),
    path('car/', views.car, name='car'),
    path('car/car_details/<int:id>/', views.car_details, name='car_details'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-history/', views.order_history, name='order_history'),

    path('Cars/', CarsListCreate.as_view(), name='CarList'),
    path('Cars/<int:pk>/', CarsDetail.as_view(), name='CarDetail'),
    path('Blog/', BlogListCreate.as_view(), name='BlogList'),
    path('Blog/<int:pk>/', BlogDetail.as_view(), name='BlogDetail'),

    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('ProtectedAPI/', views.ProtectedAPI, name='ProtectedAPI'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
