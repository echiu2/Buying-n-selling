from django.conf.urls import url
from django.urls import re_path, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'myapp'
urlpatterns = [
    path('cart/', views.cart, name='cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)