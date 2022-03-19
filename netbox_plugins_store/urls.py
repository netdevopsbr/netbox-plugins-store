"""netbox_plugins_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include
from django.urls import path, re_path

from . import views

urlpatterns = [
    # Base views
    path('', views.HomeView.as_view(), name='home'),
    path('community', views.NetboxCommunity.as_view(), name='community'),
    path('plugin_development', views.PluginDevelopmentView.as_view(), name='plugin_development'),
    path('plugin_development/readthedocs', views.ReadTheDocsGuideView.as_view(), name='readthedocs'),
    path('plugin_development/github', views.GitHubGuideView.as_view(), name='github'),

    # Django Admin
    path('admin/', admin.site.urls),
]
