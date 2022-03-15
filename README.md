# netbox-plugins-store
Easily find a useful Netbox Plugin for your environment!

## 1. Installation

The instructions below detail the process for installing and enabling **Netbox Plugins Store** plugin.
The plugin is available as a Python package in pypi and can be installed with pip.

### 1.1. Install package

Enter Netbox's virtual environment.
```
source /opt/netbox/venv/bin/activate
```

#### 1.1.1. Using git (development use)
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

### 1.3. Run Database Migrations
**OBS:** You **must** be inside Netbox's Virtual Environment (venv)
```
cd /opt/netbox/netbox/
python3 manage.py migrate
```

---

### 1.4. Restart WSGI Service

Restart the WSGI service to load the new plugin:
```
# sudo systemctl restart netbox
```

## 2. Plugin Images
![image](https://user-images.githubusercontent.com/24397251/158457301-88810934-d189-4a62-ac04-005ac0ab2bae.png)

## 3. Roadmap
- **Download** and **Install** buttons, allowing to install plugins without having to go to Netbox and configure manually on PLUGINS_CONFIG
- **Individual Plugin Page** so that Plugin Maintainers could add extra content to its plugin.

