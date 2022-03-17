
<div align=center>
  
![netbox-plugins-store](https://user-images.githubusercontent.com/24397251/158641627-7c57aa11-aa3b-4ee4-960b-87eafc314535.png)
</div>

<br>

# netbox-plugins-store
Easily find a useful Netbox Plugin for your environment!
> The **Netbox Plugins Store** supports **[Netbox v3.2 (beta version)](https://github.com/netbox-community/netbox/releases/tag/v3.2-beta2)**
---

## Summary
[1. Installation](#1-installation)
- [1.1. Install package](#11-install-package)
  - [1.1.1. Enter Netbox's virtual environment](#111-enter-netboxs-virtual-environment)
  - [1.1.2. Using git (development use)](#112-using-git-development-use)
- [1.2. Enable the Plugin](#12-enable-the-plugin)
- [1.3. Configure Plugin](#13-configure-plugin)
  - [1.3.1. Change Netbox 'settings.py' to include Netbox Plugin Store Template directory](#131-change-netbox-settingspy-to-include-netbox-plugin-store-template-directory)
- [1.4. Run Database Migrations](#14-run-database-migrations)
- [1.5 Restart WSGI Service](#15-restart-wsgi-service)

[2. Plugins Images](#2-plugin-images)

[3. Roadmap](#3-roadmap)

---

## 1. Installation

The instructions below detail the process for installing and enabling **Netbox Plugins Store** plugin.
The plugin is available as a Python package in pypi and can be installed with pip.

### 1.1. Install package

#### 1.1.1. Enter Netbox's virtual environment
```
source /opt/netbox/venv/bin/activate
```

#### 1.1.2. Using git (development use)
**OBS:** This method is recommend for testing and development purposes and is not for production use.

Move to netbox main folder
```
cd /opt/netbox/netbox
```

Clone **netbox-plugins-store** repository
```
git clone https://github.com/emersonfelipesp/netbox-plugins-store
```

Install **netbox-plugins-store**
```
cd netbox-plugins-store
source /opt/netbox/venv/bin/activate
python3 setup.py develop
```

---

### 1.2. Enable the Plugin

Enable the plugin in **/opt/netbox/netbox/netbox/configuration.py**:
```python
PLUGINS = ['netbox_plugins_store']
```

### 1.3. Configure Plugin

<br>

#### 1.3.1. Change Netbox '**[settings.py](https://github.com/netbox-community/netbox/blob/develop/netbox/netbox/settings.py)**' to include Netbox Plugin Store Template directory

> Probably on the next release of Netbox, it will not be necessary to make the configuration below! As the [Pull Request #8733](https://github.com/netbox-community/netbox/pull/8734) got merged to develop branch

Edit **/opt/netbox/netbox/netbox** and find TEMPLATE_DIR section

- How it is configured:
```python
TEMPLATES_DIR = BASE_DIR + '/templates'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'netbox.context_processors.settings_and_registry',
            ],
        },
    },
]
```

<br>

- How it is must be:
```python
TEMPLATES_DIR = BASE_DIR + '/templates'

# PROXBOX CUSTOM TEMPLATE
PLUGINSTORE_TEMPLATE_DIR = BASE_DIR + '/netbox-plugins-store/netbox_plugins_store/templates/netbox_plugins_store'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR, PLUGINSTORE_TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'netbox.context_processors.settings_and_registry',
            ],
        },
    },
]
```
I did it because I had to change the **base/layout.html** from Netbox, since there is no **Jinja2 block** to fill with custom information into the **footer HTML tag**

### 1.4. Run Database Migrations
**OBS:** You **must** be inside Netbox's Virtual Environment (venv)
```
cd /opt/netbox/netbox/
python3 manage.py migrate
```



---

### 1.5. Restart WSGI Service

Restart the WSGI service to load the new plugin:
```
sudo systemctl restart netbox
```

## 2. Plugin Images
![image](https://user-images.githubusercontent.com/24397251/158582710-9ce597f4-d051-4381-8e27-96db1dc50c61.png)

## 3. Roadmap
- **Download** and **Install** buttons, allowing to install plugins without having to go to Netbox and configure manually on PLUGINS_CONFIG
- **Individual Plugin Page** so that Plugin Maintainers could add extra content to its plugin.

