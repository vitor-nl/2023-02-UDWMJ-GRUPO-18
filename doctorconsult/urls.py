"""doctorconsult URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from patient.views import LoginPageView
from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('attendant/', include('attendant.urls', namespace='attendant')),
    # path('person/', include('person.urls', namespace='person')),
    # path('consult/', include('consult.urls', namespace='consult')),
    # path('patient/', include('patient.urls', namespace='patient')),
    
    path('admin/', admin.site.urls),
    path('attendant/', include('attendant.urls')),
    path('person/', include('person.urls')),
    path('consult/', include('consult.urls')),
    path('patient/', include('patient.urls')),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='login.html'), name='home'),
    path('', LoginPageView.as_view(), name='index'),  
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    
    #templates:
    
    # path("chat/", include("apps.chat.urls")),
    # path('admin/', admin.site.urls),
]   