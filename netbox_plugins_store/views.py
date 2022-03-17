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
                "repos_name": github.repos_name,
            }
        )

class PluginPageView(View):
    """Homepage"""
    template_name = 'netbox_plugins_store/pluginpage.html'

    # service incoming GET HTTP requests
    def get(self, request, **url_params):
        name = url_params.get('name', 'default')

        github_json = github.search_github_json(name)

        """Get request."""
        return render(
            request,
            self.template_name,
            {
                "plugin_name": name,
                "github": github_json,
            }
        )