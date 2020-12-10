from django.urls import path, include
from . import views

app_name='articles'

urlpatterns = [
    path('', views.article_homepage, name='list'),
    path('<id>', views.article_detail, name='detail'),
    path('owner/<id>', views.article_detail_own, name='detailowned'),
    path('create/', views.article_create, name='create'),
    path('my-article/', views.article_owned, name='owned'),
    path('create/<int:id>/', views.article_create, name='create'),
    path('delete/<int:id>/', views.article_delete, name='delete'),
]
