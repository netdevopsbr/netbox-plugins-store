# Netbox plugin related import
from extras.plugins import PluginConfig

class PluginsStoreConfig(PluginConfig):
    name = "netbox_plugins_store"
    verbose_name = "Netbox Plugins Store"
    description = "Easily find a useful Netbox Plugin for your environment!"
    version = "0.0.1"
    author = "Emerson Felipe (@emersonfelipesp) / Marcos Vella (@marcosvella)"
    author_email = "emerson.felipe@nmultifibra.com.br"
    base_url = "netbox_plugins_store"
    required_settings = []
    default_settings = {
        'github_url': 'https://github.com',
        'github_api_url': 'http://api.github.com',
        'authorization': 'token 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',
    }

config = PluginsStoreConfig