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


class ExternalLinkView(View):
    """Homepage"""
    template_name = 'netbox_plugins_store/external_link.html'

    # External URL's related to Netbox
    external_urls = {
        "plugin": {
            "readthedocs": "https://netbox.readthedocs.io/en/feature/plugins/development/",
            "github-tutorial": "https://github.com/netbox-community/netbox-plugin-tutorial"
        },
        "community": {
            "slack": "https://netdev.chat/",
            "github_discussion": "https://github.com/netbox-community/netbox/discussions",
            "brazil": {
                "telegram": "https://t.me/netboxbr",
                "discord": "https://discord.gg/Zp9YQ67j"
            }
        }
    }
    # service incoming GET HTTP requests
    def get(self, request, **url_params):
        external_urls = self.external_urls

        # HTTP Request Parameters
        category = url_params.get('category', 'default')
        country = url_params.get('country', 'empty')
        name = url_params.get('name', 'default')

        if category != 'default':
            if country != 'empty':
                if name != 'default':
                    try:
                        url = external_urls.get(category).get(country).get(name)
                    except:
                        url = 'plugins:netbox_plugins_store:home'
        else:
            url = 'plugins:netbox_plugins_store:home'
        """Get request."""
        return redirect(url)

class CommunitySlack(View):
    """Netbox Slack Official Community"""
    external_url = 'https://netdev.chat/'

    def get(self, request):
        return redirect(self.external_url)


class CommunityGitHubDiscussion(View):
    """Netbox Slack Official Community"""
    external_url = 'https://github.com/netbox-community/netbox/discussions'
    
    def get(self, request):
        return redirect(self.external_url)


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
