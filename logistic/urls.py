from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),

    path('registration_modal/', views.registration_modal, name='registration_modal'),
    path('auth_modal/', views.auth_modal, name='auth_modal'),
    path('logout_user/', views.logout_user, name='logout_user'),

    path('get_and_send_ti_admin/', views.get_and_send_ti_admin, name='get_and_send_ti_admin'),
    
    path('get_order_data/', views.get_order_data, name='get_order_data'),
]