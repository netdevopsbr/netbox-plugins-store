from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_plugins_store:home',
        link_text='Netbox Plugins',
    ),
    PluginMenuItem(
        link='plugins:netbox_plugins_store:pluginpage',
        link_text='Plugin Page',
    ),
)
