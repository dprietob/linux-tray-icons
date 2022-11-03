#!/usr/bin/python
import os
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator


def main():
    # localdevtray is the ID of the tray indicator. It must be unique for each tray icon.
    # applications-development-symbolic is the tray icon and can be changed by any icon of your system.
    indicator = appindicator.Indicator.new("localdevtray", "applications-development-symbolic",
                                           appindicator.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(menu())
    gtk.main()


def menu():
    menu = gtk.Menu()

    # MySQL option
    handle_mysql = gtk.CheckMenuItem(label="MySQL service")
    handle_mysql.set_active(is_mysql_active())
    handle_mysql.connect("activate", update_mysql)
    menu.append(handle_mysql)

    # Memcached option
    handle_memcached = gtk.CheckMenuItem(label="MemCached service")
    handle_memcached.set_active(is_memcached_active())
    handle_memcached.connect("activate", update_memcached)
    menu.append(handle_memcached)
    
    # Varnish option
    handle_varnish = gtk.CheckMenuItem(label="Varnish service")
    handle_varnish.set_active(is_varnish_active())
    handle_varnish.connect("activate", update_varnish)
    menu.append(handle_varnish)

    # Apache2 option
    handle_apache2 = gtk.CheckMenuItem(label="Apache2 service")
    handle_apache2.set_active(is_apache_active())
    handle_apache2.connect("activate", update_apache2)
    menu.append(handle_apache2)

    # PHP 7.2-fpm option
    handle_php72fpm = gtk.CheckMenuItem(label="PHP 7.2-fpm service")
    handle_php72fpm.set_active(is_php72fpm_active())
    handle_php72fpm.connect("activate", update_php72fpm)
    menu.append(handle_php72fpm)

    # PHP 7.4-fpm option
    handle_php74fpm = gtk.CheckMenuItem(label="PHP 7.4-fpm service")
    handle_php74fpm.set_active(is_php74fpm_active())
    handle_php74fpm.connect("activate", update_php74fpm)
    menu.append(handle_php74fpm)

    # PHP 8.1-fpm option
    handle_php81fpm = gtk.CheckMenuItem(label="PHP 8.1-fpm service")
    handle_php81fpm.set_active(is_php81fpm_active())
    handle_php81fpm.connect("activate", update_php81fpm)
    menu.append(handle_php81fpm)

    menu.show_all()
    return menu


def update_mysql(_):
    if _.get_active():
        os.system("systemctl start mysql")
    else:
        os.system("systemctl stop mysql")

def update_memcached(_):
    if _.get_active():
        os.system("systemctl start memcached")
    else:
        os.system("systemctl stop memcached")
        
def update_varnish(_):
    if _.get_active():
        os.system("systemctl start varnish")
    else:
        os.system("systemctl stop varnish")

def update_apache2(_):
    if _.get_active():
        os.system("systemctl start apache2")
    else:
        os.system("systemctl stop apache2")


def update_php72fpm(_):
    if _.get_active():
        os.system("systemctl start php7.2-fpm")
    else:
        os.system("systemctl stop php7.2-fpm")


def update_php74fpm(_):
    if _.get_active():
        os.system("systemctl start php7.4-fpm")
    else:
        os.system("systemctl stop php7.4-fpm")


def update_php81fpm(_):
    if _.get_active():
        os.system("systemctl start php8.1-fpm")
    else:
        os.system("systemctl stop php8.1-fpm")


def is_mysql_active():
    return os.system("systemctl status mysql --no-pager") == 0

def is_memcached_active():
    return os.system("systemctl status memcached --no-pager") == 0
    
def is_varnish_active():
    return os.system("systemctl status varnish --no-pager") == 0

def is_apache_active():
    return os.system("systemctl status apache2 --no-pager") == 0


def is_php72fpm_active():
    return os.system("systemctl status php7.2-fpm --no-pager") == 0


def is_php74fpm_active():
    return os.system("systemctl status php7.4-fpm --no-pager") == 0


def is_php81fpm_active():
    return os.system("systemctl status php8.1-fpm --no-pager") == 0


if __name__ == "__main__":
    main()
