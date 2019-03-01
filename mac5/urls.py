"""mac5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.conf.urls import include, url
from django.conf.urls.static import static
from mac5 import settings
from homepage.views import home

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', home),
    url('form-elements/', TemplateView.as_view(template_name='form-elements.html')),
    url('administration/', include('administration.urls')),
    url('homepage/', include('homepage.urls')),
    url('servicespage/', include('servicespage.urls')),
    url('contactpage/', include('contactpage.urls')),
    url('header/', include('header.urls')),
    url('quemsomos/', include('whoweare.urls'))
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
