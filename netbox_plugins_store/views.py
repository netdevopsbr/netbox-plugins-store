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
                "github": github.repositories,
            }
        )


class NetboxCommunity(View):
    """Plugins Development Tutorial"""

    template_name = 'netbox_plugins_store/community.html'

    # service incoming GET HTTP requests
    def get(self, request):
        """Get request."""
        return render(
            request,
            self.template_name,
        )


class PluginDevelopmentView(View):
    """Plugins Development Tutorial"""

    template_name = 'netbox_plugins_store/plugin_development.html'

    # service incoming GET HTTP requests
    def get(self, request):
        """Get request."""
        return render(
            request,
            self.template_name,
        )


class ReadTheDocsGuideView(View):
    """Plugins Development Tutorial - ReadTheDocs"""

    def get(self, request):
        return redirect('https://netbox.readthedocs.io/en/feature/plugins/development/')


class GitHubGuideView(View):
    """Plugins Development Tutorial - GitHub"""

    def get(self, request):
        return redirect('https://github.com/netbox-community/netbox-plugin-tutorial')