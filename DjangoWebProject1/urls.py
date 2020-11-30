"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path

from django.urls import include
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('links/', views.links, name='links'),
    path('about/', views.about, name='about'),
    path('pool/', views.pool, name='pool'),
    path('video/', views.video, name='video'),
    path('blog/', views.blog, name='blog'),
    path('newpost/', views.newpost, name='newpost'),
    path('(?P<parametr>\d+)/', views.blogpost, name='blogpost'),
    path('registration/', views.registration, name='registration'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Вход',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()