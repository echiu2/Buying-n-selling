from django.conf.urls import url
from django.urls import re_path, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'listings'
urlpatterns = [
    path('addPost/', views.addPost, name='addPost'),
    path('listing_submission/', views.listing_submission, name='listing_submission')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)