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
            PluginMenuButton('plugins:netbox_plugins_store:external_links', 'Plugins Development - ReadTheDocs', 'mdi mdi-file-document-multiple', ButtonColorChoices.BLUE),
            PluginMenuButton('plugins:netbox_plugins_store:external_links', 'Plugins Development - GitHub', 'mdi mdi-github', ButtonColorChoices.BLACK),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_plugins_store:community',
        link_text='Netbox Community',
        buttons=(
            PluginMenuButton('plugins:netbox_plugins_store:slack', 'Official Slack Community', 'mdi mdi-slack', ButtonColorChoices.RED),
            PluginMenuButton('plugins:netbox_plugins_store:github_discussion', 'GItHub Discussions', 'mdi mdi-github', ButtonColorChoices.BLACK),
        )
    ),
)
