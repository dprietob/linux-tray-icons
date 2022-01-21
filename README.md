# Linux Tray Icons
This script allows add tray icons with submenus and options in __Linux Wing Panel__. The following will detail how to configure it to run on system boot.

![](https://i.ibb.co/zHrhHTr/screenshot.png)

## Warning
These steps have been performed only on the __Elementary OS 6.1__ distribution. I do not know if it could give failures in other Linux distributions.

## Note
This documentation uses ``python`` command to run and compile Python scripts. This command may be different on your system (e.g. ``python3``). You should use whatever command is available to you.

## Configuration
First of all, it's necessary install [Wingpanel Ayatana-Compatibility Indicator](https://github.com/Lafydev/wingpanel-indicator-ayatana) on your system if it is not already installed. Afterwards, you can open the script with any code editor and modify it to add options according to your needs. The script is very short and simple and includes some commented features by default, so it will not be difficult for you to understand how it works.

## Installation
Once configured to your liking, you can run the script directly using:
```
python linux-tray-icon.py
```
If you don't want to have to run this command every time you boot your system, you can tell your Linux distribution to run it for you. To do this, compile the script to generate a ``.pyc`` file using the command:
```
python -m your-tray-icon linux-tray-icon.py
```
Once the ``.pyc`` file is generated, you will need to make it executable using the following command (this is probably not necessary since the script includes the ``#!/usr/bin/python`` statement, but just in case):
```
chmod +x your-tray-icon.pyc
```
Next, move the ``.pyc`` file to the ``~.local/bin/`` directory on your system, and then create a ``.desktop`` file inside the ``~.config/autostart/`` directory with the following content:
```
[Desktop Entry]
Name=YourTrayIconName
GenericName=Your tray icon generic name
Comment=Your tray icon description
Exec=your-tray-icon.pyc
Terminal=false
Type=Application
Icon=your-tray-system-icon
Categories=Utility;
Keywords=shorcut;app;
StartupNotify=false
X-GNOME-Autostart-enabled=true
```
Obviously, the ``Name``, ``GenericName``, ``Comment``, ``Exec``, ``Icon``, ``Category`` and ``Keywords`` sections must be configured according to your needs.

This should make the application recognized by the system and available to start at system boot.
![](https://i.ibb.co/rkMN5Hd/system-boot.png)
