import platform
import sys

from django.conf import settings
from django.shortcuts import redirect, render

from django.template import loader
from django.template.exceptions import TemplateDoesNotExist

from django.urls import reverse

from django.views.generic import View

from . import repositories

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
                "github": repositories.github_json,
            }
        )