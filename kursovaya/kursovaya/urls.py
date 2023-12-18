"""kursovaya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
import views

urlpatterns = [
    path('', views.auth),
    path('registration', views.reg),
    path('main_a', views.main_a),
    path('main_u', views.main_u),
    path('about', views.description),
    path('all_auto', views.all_auto),
    path('auto/<str:autoid>', views.auto),
    path('search/', views.search),
    path('redaction', views.redact),
    path('add_auto', views.add_auto),
    path('delete_auto', views.delete_auto),
    path('add_user', views.add_user),
    path('delete_user', views.delete_user)
]
