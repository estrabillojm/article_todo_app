from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from accounts import views as account_views

urlpatterns = [
    path('admin/jme/', admin.site.urls),
    path('', account_views.account_login),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)