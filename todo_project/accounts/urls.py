from django.urls import path, include
from . import views

app_name='accounts'

urlpatterns = [
    path('', views.account_login, name='login'),
    path('signup/', views.account_signup, name='signup'),
    path('logout/', views.account_logout, name='logout'),
]
