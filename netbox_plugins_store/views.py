import platform
import sys

from django.conf import settings
from django.shortcuts import redirect, render

from django.template import loader
from django.template.exceptions import TemplateDoesNotExist

from django.urls import reverse

from django.views.generic import View

from netbox_plugins_store.github_api import github

class HomeView(View):
    """Homepage"""
    template_name = 'netbox_plugins_store/home.html'

    # service incoming GET HTTP requests
    def get(self, request):
        """Get request."""
        return render(
            request,
            self.template_name,
            {
                "github": github.repos_json_summary,
            }
        )

class NetboxPluginPage(View):
    """Netbox Plugin Page to render specific contet of the Plugin"""
    template_name = 'netbox_plugins_store/teste.html'

    # service incoming GET HTTP requests
    def get(self, request, **kwargs):
        # Get Plugin Name from URL
        plugin_name = kwargs.get('name')

        # Get request.
        return render(
            request,
            'netbox_plugins_store/teste2.html',
            {
                "plugin_name": plugin_name,
            }
        )