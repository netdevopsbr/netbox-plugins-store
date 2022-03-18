from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_plugins_store:home',
        link_text='Netbox Plugins',
    ),
    PluginMenuItem(
        link='plugins:netbox_plugins_store:plugin_development',
        link_text='Plugins Development',
        buttons=(
            PluginMenuButton('plugins:netbox_plugins_store:readthedocs', 'Plugins Development - ReadTheDocs', 'mdi mdi-file-document-multiple', ButtonColorChoices.BLUE),
            PluginMenuButton('plugins:netbox_plugins_store:github', 'Plugins Development - GitHub', 'mdi mdi-github', ButtonColorChoices.BLACK),
        )
    ),
)
