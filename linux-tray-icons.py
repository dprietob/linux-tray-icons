#!/usr/bin/python
import os
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

def main():
    indicator = appindicator.Indicator.new("localdevtray", "applications-development-symbolic", appindicator.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(menu())
    gtk.main()

def menu():
    menu = gtk.Menu()

    handle_vpn = gtk.CheckMenuItem(label="Conexión VPN")
    handle_vpn.set_active(is_vpn_active())
    handle_vpn.connect("activate", update_vpn)
    menu.append(handle_vpn)

    menu.append(gtk.SeparatorMenuItem())

    handle_mysql = gtk.CheckMenuItem(label="Servicio MySQL")
    handle_mysql.set_active(is_mysql_active())
    handle_mysql.connect("activate", update_mysql)
    menu.append(handle_mysql)

    handle_apache2 = gtk.CheckMenuItem(label="Servicio Apache2")
    handle_apache2.set_active(is_apache_active())
    handle_apache2.connect("activate", update_apache2)
    menu.append(handle_apache2)

    handle_php72fpm = gtk.CheckMenuItem(label="Servicio PHP 7.2-fpm")
    handle_php72fpm.set_active(is_php72fpm_active())
    handle_php72fpm.connect("activate", update_php72fpm)
    menu.append(handle_php72fpm)

    handle_php74fpm = gtk.CheckMenuItem(label="Servicio PHP 7.4-fpm")
    handle_php74fpm.set_active(is_php74fpm_active())
    handle_php74fpm.connect("activate", update_php74fpm)
    menu.append(handle_php74fpm)

    handle_php81fpm = gtk.CheckMenuItem(label="Servicio PHP 8.1-fpm")
    handle_php81fpm.set_active(is_php81fpm_active())
    handle_php81fpm.connect("activate", update_php81fpm)
    menu.append(handle_php81fpm)

    menu.append(gtk.SeparatorMenuItem())

    exit_item = gtk.MenuItem(label="Salir")
    exit_item.connect("activate", quit)
    menu.append(exit_item)

    menu.show_all()
    return menu

def update_vpn(_):
    if _.get_active():
        os.system("systemctl start openvpn")
    else:
        os.system("systemctl stop openvpn")

def update_mysql(_):
    if _.get_active():
        os.system("systemctl start mysql")
    else:
        os.system("systemctl stop mysql")

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

def quit(_):
    gtk.main_quit()

def is_vpn_active():
    return os.system("systemctl status openvpn --no-pager") == 0

def is_mysql_active():
    return os.system("systemctl status mysql --no-pager") == 0

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
